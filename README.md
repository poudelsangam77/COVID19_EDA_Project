# COVID-19 Exploratory Data Analysis (EDA) Project

## Project Overview
This project performs **Exploratory Data Analysis (EDA)** on global and country-level **COVID-19 data**. Through various visualizations and statistical techniques, this project aims to:
- Analyze COVID-19 trends globally and locally (by country).
- Understand key features of the data such as infection rates, mortality rates, and vaccination progress.
- Identify patterns, outliers, and correlations in the dataset.
- Create actionable insights using various plots and reports.

## Project Goal
The goal of this project is to provide clear insights into the **spread and impact of COVID-19** worldwide. Key questions addressed include:
- What are the most affected regions by COVID-19?
- How have case numbers and deaths evolved over time?
- What are the trends in COVID-19 vaccination?

## Technologies Used
- **Python**: For data processing and analysis.
  - Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`
- **Jupyter Notebook**: For running and documenting the analysis.
- **Dash/Plotly**: For creating interactive dashboards (optional).
- **Git**: For version control and collaboration.
- **GitHub**: For repository hosting and sharing.

## Dataset
This project utilizes COVID-19 datasets from various reliable sources like:
- [Johns Hopkins University COVID-19 Dataset](https://github.com/CSSEGISandData/COVID-19)
- [Our World in Data](https://github.com/owid/covid-19-data)
- [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)

### **Dataset Sources**
- **COVID-19 confirmed cases**: Case data reported globally and at the country level.
- **Deaths and recoveries**: Information on the number of deaths and recoveries.
- **Vaccination data**: Global and country-wise vaccination statistics.

## Folder Structure

The project structure is organized as follows:

COVID19_EDA_Project/
├── data/                     
│   ├── raw/               # Raw data files
│   └── processed/         # Cleaned data files
├── notebooks/              
│   ├── data_cleaning.ipynb   # Notebook for cleaning data
│   ├── exploratory_analysis.ipynb  # Notebook for exploratory analysis
│   └── visualizations.ipynb  # Notebook for generating visualizations
├── dashboard/               # (Optional) Dash app files for interactive visualizations
├── reports/
│   └── visuals/            # Saved visualizations for reports
├── .gitignore               # Git ignore file for system files and caches
├── LICENSE                  # License file for the project
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies

### **Folder Details**
- **`data/raw/`**: Raw datasets that are downloaded and need processing.
- **`data/processed/`**: Cleaned and transformed data that will be used for analysis.
- **`notebooks/`**: Jupyter notebooks that contain the code for the EDA process, visualizations, and conclusions.
- **`dashboard/`**: (Optional) Files for building interactive visualizations using Dash.
- **`reports/visuals/`**: Saved visualizations (e.g., PNG, PDF files) for reports and presentations.

## Installation

Follow the steps below to get your local development environment up and running.

### **1. Clone the Repository**
Clone the repository to your local machine using Git:

```bash
git clone https://github.com/poudelsangam77/COVID19_EDA_Project.git
cd COVID19_EDA_Project
