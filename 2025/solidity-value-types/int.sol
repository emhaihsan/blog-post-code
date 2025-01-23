// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SignedIntegerExample {
    int8 public a = 10;
    int16 public b = 50;

    int256 public c = a - b; // result: -40
}
