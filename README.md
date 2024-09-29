# Assignment2_Conveory_inspection

## Project Overview

The **Conveyory Inspection** project implements a user interface (UI) for inspecting defects in conveyor operations. The system uses a Python-based UI, which runs a background algorithm for defect detection, while simultaneously displaying the latest defects and the last 50 recorded defects.

This project is designed to streamline defect tracking and enhance operational efficiency in conveyor systems.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Running the UI](#running-the-ui)
- [Background Algorithm](#background-algorithm)
- [Contributing](#contributing)
- [License](#license)

## Features

- User-friendly interface for real-time defect inspection.
- Background processing of defect detection algorithms.
- Displays the latest defects and a log of the last 50 records.
- Ability to cut and manipulate video feeds for inspection.

## Requirements

- Python 3.8 or higher
- PyQt5
- YOLOV8
- psycopg2 (or any other database connector you may use)
- OpenCV

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Assignment2_Conveyory_Inspection.git
   cd Assignment2_Conveyory_Inspection

Running the UI

cd Ui
python3 Main_v1.py

