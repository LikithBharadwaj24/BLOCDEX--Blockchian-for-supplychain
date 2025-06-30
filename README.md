# 📦 BLOCDEX – Blockchain for Supply Chain

**BLOCDEX** is a blockchain-based supply chain solution that leverages the power of decentralization, immutability, and transparency to securely track the movement and ownership of products across the supply chain.

This project was developed using **Solidity**, **Truffle**, and **Ganache**, with the goal of improving traceability, reducing fraud, and enhancing trust among stakeholders in a distributed supply chain network.

---

## 🚀 Features

- ✅ Product information management on-chain
- ✅ User registration and verification
- ✅ Immutable purchase history records
- ✅ Smart contract-based identity and ownership tracking
- ✅ Deployable on Ethereum-compatible networks
- ✅ Local testing with Ganache & Truffle

---

## 🛠️ Technologies Used

| Layer | Tools/Tech |
|------|------------|
| **Smart Contracts** | Solidity, Truffle |
| **Local Blockchain** | Ganache |
| **Frontend** *(optional)* | React, Web3.js |
| **Wallet Integration** | MetaMask |
| **Version Control** | Git & GitHub |

---

## 📁 Project Structure

BLOCDEX--Blockchian-for-supplychain/
├── contracts/
│ ├── ProductInfo.sol
│ ├── UsersInfo.sol
│ └── PurchaseHistory.sol
├── migrations/
├── test/
├── build/
├── truffle-config.js
├── README.md
└── .gitignore



---

## 🧪 Getting Started (Local Setup)

### 1. Clone the repository
```bash
git clone https://github.com/LikithBharadwaj24/BLOCDEX--Blockchian-for-supplychain.git
cd BLOCDEX--Blockchian-for-supplychain

2. Install dependencies
bash
Copy
Edit
npm install
3. Start Ganache (or Ganache CLI)
Make sure Ganache is running on port 7545.

4. Compile and deploy smart contracts
bash
Copy
Edit
truffle compile
truffle migrate --reset
5. Run tests (if available)
bash
Copy
Edit
truffle test
