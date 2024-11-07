// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract Houses {
    struct House {
        uint id;
        string houseAddress;
        uint price;
        address payable owner;
        bool availability;
    }

    mapping(uint => House) public housesList;
    mapping(address => uint) public sellerBalance;
    uint public housesCount;

    IERC20 public token;

    event HouseAdded(uint id, string homeAddress, uint price, address owner);
    event HouseTransaction(uint id, address buyer, uint price);

    constructor(address _tokenAddress) {
        token = IERC20(_tokenAddress); // Set token contract address
    }

    function addHouse(string memory _houseAddress, uint _price) public {
        require(_price > 0, "Price must be above 0");

        housesCount++;

        housesList[housesCount] = House(
            housesCount,
            _houseAddress,
            _price,
            payable(msg.sender),
            true
        );

        emit HouseAdded(housesCount, _houseAddress, _price, msg.sender);
    }

    function buyHouse(uint _id) public {
        House storage house = housesList[_id];

        require(house.availability, "House not available");
        require(token.balanceOf(msg.sender) >= house.price, "Insufficient token balance");
        require(house.owner != msg.sender, "Cannot buy your own house");

        // Transfer tokens from buyer to seller
        require(token.transferFrom(msg.sender, house.owner, house.price), "Token transfer failed");

        // Update house ownership and availability
        house.owner = payable(msg.sender);
        house.availability = false;

        emit HouseTransaction(_id, msg.sender, house.price);
    }
}
