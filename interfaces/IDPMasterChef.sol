// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

interface IDPMasterChef {
    function userInfo(uint256 pid, address user) external view returns ( uint256  amount, uint256  rewardDebt, uint256  lastDepositTime, uint256  withdrawTimes, uint256  lastWithdrawTime );
}