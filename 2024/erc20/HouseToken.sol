// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract HouseToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("HouseToken", "HTK") {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }
}
