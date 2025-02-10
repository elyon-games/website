#!/bin/bash

echo "Installing Node.js dependencies..."
npm install

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Installation complete."
read -p "Press any key to continue..."