# Real Estate Marketplace with Custom Token

This repository contains Solidity smart contracts for a decentralized real estate marketplace. The marketplace allows users to list and purchase properties using a custom ERC-20 token (`HouseToken`).

## Overview

The project includes two main smart contracts:

1. **HouseToken**: A custom ERC-20 token used as the currency for transactions within the marketplace.
2. **Houses**: A marketplace contract that allows users to list their houses for sale and purchase houses using the `HouseToken`.

### Contracts

1. **HouseToken.sol**
   - This contract defines a custom ERC-20 token named "HouseToken" with the symbol "HTK".
   - The token can be minted with an initial supply set during deployment.
2. **Houses.sol**
   - This contract implements a simple marketplace where users can list houses for sale and buy listed houses using `HouseToken`.
   - Users can list houses by specifying an address and a price, and others can buy the house if they have enough `HouseToken` balance.

## Contract Details

### HouseToken

The `HouseToken` contract is an ERC-20 token that:

- Uses OpenZeppelin's ERC-20 implementation.
- Mints an initial supply to the contract deployer upon deployment.

#### Constructor

```solidity
constructor(uint256 initialSupply)
```

- `initialSupply`: The initial amount of tokens to mint for the deployer, adjusted with decimals (10^18).

### Houses

The `Houses` contract manages a marketplace where users can add houses for sale or buy listed houses using `HouseToken`.

#### Constructor

```solidity
constructor(address _tokenAddress)
```

- `_tokenAddress`: The address of the deployed `HouseToken` contract. This token is used for all transactions in the marketplace.

#### Structs

- **House**: Stores details of each house listing.
  - `id`: Unique ID of the house.
  - `houseAddress`: Physical address or description of the house.
  - `price`: Price of the house in `HouseToken`.
  - `owner`: Current owner of the house.
  - `availability`: Indicates if the house is available for purchase.

#### Functions

- **addHouse**:

  ```solidity
  function addHouse(string memory _houseAddress, uint _price) public
  ```

  - Allows a user to list a new house for sale.
  - Emits a `HouseAdded` event upon successful listing.
  - Requirements:
    - `_price` must be greater than 0.

- **buyHouse**:
  ```solidity
  function buyHouse(uint _id) public
  ```
  - Allows a user to buy a listed house.
  - Transfers `HouseToken` from buyer to seller.
  - Updates the owner and availability of the house.
  - Emits a `HouseTransaction` event upon successful transaction.
  - Requirements:
    - House must be available for purchase.
    - Buyer must have enough `HouseToken` balance.
    - Buyer cannot be the current owner of the house.

## Events

- **HouseAdded**: Triggered when a new house is listed.

  ```solidity
  event HouseAdded(uint id, string homeAddress, uint price, address owner);
  ```

- **HouseTransaction**: Triggered when a house is successfully purchased.
  ```solidity
  event HouseTransaction(uint id, address buyer, uint price);
  ```

## Example

1. Deploy `HouseToken` with an initial supply of 1000 HTK.
2. Deploy `Houses` with the address of the deployed `HouseToken`.
3. User A calls `addHouse("123 Blockchain St", 100 HTK)`.
4. User B (who has at least 100 HTK) calls `buyHouse(1)` to purchase the listed house.
