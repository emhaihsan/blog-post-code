// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BookNFT is ERC721, Ownable {
    struct Book {
        uint256 id;
        string name;
        string author;
        address authorAddress;
        uint256 totalSupply;
        uint256 price;
        uint256 initialRoyalty;
        uint256 resaleRoyalty;
        uint256 transactionCount;
        mapping(address => uint256) ownedNFTs;
        mapping(address => uint256) resalePrices;
    }

    mapping(uint256 => Book) public books;
    mapping(uint256 => address[]) public bookOwners;

    event BookCreated(
        uint256 indexed id,
        string name,
        string author,
        address indexed authorAddress,
        uint256 totalSupply,
        uint256 price,
        uint256 initialRoyalty,
        uint256 resaleRoyalty
    );
    event NFTBought(uint256 indexed id, address indexed buyer);
    event NFTDonated(
        uint256 indexed id,
        address indexed from,
        address indexed to
    );
    event ResalePriceSet(
        uint256 indexed bookId,
        address indexed owner,
        uint256 price
    );

    constructor() ERC721("MybookNFT", "MBOOK") Ownable(msg.sender) {}

    function createBook(
        uint256 bookId,
        string memory name,
        string memory author,
        address authorAddress,
        uint256 totalSupply,
        uint256 price,
        uint256 initialRoyalty,
        uint256 resaleRoyalty
    ) external onlyOwner {
        require(books[bookId].id == 0, "Book ID already exists");
        require(
            initialRoyalty <= 100,
            "Initial royalty must be between 0 and 100"
        );
        require(
            resaleRoyalty <= 100,
            "Resale royalty must be between 0 and 100"
        );

        Book storage newBook = books[bookId];
        newBook.id = bookId;
        newBook.name = name;
        newBook.author = author;
        newBook.authorAddress = authorAddress;
        newBook.totalSupply = totalSupply;
        newBook.price = price;
        newBook.initialRoyalty = initialRoyalty;
        newBook.resaleRoyalty = resaleRoyalty;
        newBook.transactionCount = 0;

        emit BookCreated(
            bookId,
            name,
            author,
            authorAddress,
            totalSupply,
            price,
            initialRoyalty,
            resaleRoyalty
        );
    }

    uint256 private tokenCounter = 0;

    function buyNFT(uint256 bookId) external payable {
        Book storage book = books[bookId];
        require(book.price > 0, "Price not set for this NFT");
        require(msg.value >= book.price, "Insufficient funds to buy the NFT");
        require(book.totalSupply > 0, "No supply available");

        uint256 tokenId = tokenCounter + bookId;
        tokenCounter++;

        _mint(msg.sender, tokenId);
        book.ownedNFTs[msg.sender]++;
        book.transactionCount++;
        book.totalSupply--;

        uint256 royaltyAmount = (book.price * book.initialRoyalty) / 100;
        payable(book.authorAddress).transfer(royaltyAmount);

        if (
            bookOwners[bookId].length == 0 ||
            bookOwners[bookId][bookOwners[bookId].length - 1] != msg.sender
        ) {
            bookOwners[bookId].push(msg.sender);
        }

        emit NFTBought(bookId, msg.sender);
    }

    function buyResaleNFT(uint256 bookId, address owner) external payable {
        uint256 resalePrice = books[bookId].resalePrices[owner];
        require(resalePrice > 0, "This NFT is not for sale");
        require(
            msg.value >= resalePrice,
            "Insufficient funds to buy the resale NFT"
        );

        _transfer(owner, msg.sender, bookId);
        books[bookId].ownedNFTs[owner]--;
        books[bookId].ownedNFTs[msg.sender]++;

        uint256 resaleRoyaltyAmount = (resalePrice *
            books[bookId].resaleRoyalty) / 100;
        payable(books[bookId].authorAddress).transfer(resaleRoyaltyAmount);

        payable(owner).transfer(msg.value - resaleRoyaltyAmount);
        books[bookId].transactionCount++;

        emit NFTBought(bookId, msg.sender);
    }

    function donateNFT(uint256 bookId, address to) external {
        require(
            _isApprovedOrOwner(msg.sender, bookId),
            "Not the owner or approved"
        );

        _transfer(msg.sender, to, bookId);
        books[bookId].ownedNFTs[msg.sender]--;
        books[bookId].ownedNFTs[to]++;

        emit NFTDonated(bookId, msg.sender, to);
    }

    function setResalePrice(uint256 bookId, uint256 price) external {
        require(
            _isApprovedOrOwner(msg.sender, bookId),
            "Not the owner or approved"
        );
        require(
            books[bookId].ownedNFTs[msg.sender] > 0,
            "You don't own this NFT"
        );

        books[bookId].resalePrices[msg.sender] = price;
        emit ResalePriceSet(bookId, msg.sender, price);
    }

    function cancelResalePrice(uint256 bookId) external {
        require(
            _isApprovedOrOwner(msg.sender, bookId),
            "Not the owner or approved"
        );
        require(
            books[bookId].ownedNFTs[msg.sender] > 0,
            "You don't own this NFT"
        );

        books[bookId].resalePrices[msg.sender] = 0;
    }

    function getResalePrice(
        uint256 bookId,
        address owner
    ) external view returns (uint256) {
        return books[bookId].resalePrices[owner];
    }

    function getNFTPurchaseInfo(
        uint256 bookId
    ) external view returns (uint256 purchased, uint256 totalSupply) {
        Book storage book = books[bookId];
        uint256 totalPurchased = book.transactionCount;
        uint256 totalBookSupply = book.totalSupply + book.transactionCount;

        return (totalPurchased, totalBookSupply);
    }

    function getTransactionCount(
        uint256 bookId
    ) external view returns (uint256) {
        return books[bookId].transactionCount;
    }

    function getUniqueOwners(uint256 bookId) external view returns (uint256) {
        return bookOwners[bookId].length;
    }

    function _isApprovedOrOwner(
        address spender,
        uint256 tokenId
    ) internal view returns (bool) {
        address owner = ownerOf(tokenId);
        return (spender == owner ||
            isApprovedForAll(owner, spender) ||
            getApproved(tokenId) == spender);
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
