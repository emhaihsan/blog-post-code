// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract UnsignedIntegerExample {
    uint8 public a = 100; // 0 -> 255
    uint16 public b = 10000; // 0 -> 65535

    // uint is an alias for uint256
    uint public c = 1000000000000;
    uint256 public d = 1000000000000;
}
