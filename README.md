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
- **Dash/Plotly**: For creating interactive dashboards.
- **Git**: For version control and collaboration.
- **GitHub**: For repository hosting and sharing.

## Dataset

This project utilizes **multiple datasets** from various reliable sources to perform an exploratory data analysis of COVID-19 trends globally and at the country level. The following datasets are used in this project:

### Dataset Sources:
1. **Johns Hopkins University COVID-19 Dataset**
   - **Source**: [GitHub Repository - Johns Hopkins University COVID-19](https://github.com/CSSEGISandData/COVID-19)
   - **Description**: This dataset contains daily reports of confirmed COVID-19 cases, deaths, and recoveries at a global level and by country.
   - **Data Included**: 
     - Confirmed cases
     - Deaths and recoveries
     - Geographical information (e.g., country, province)

2. **Our World in Data COVID-19 Dataset**
   - **Source**: [GitHub Repository - Our World in Data COVID-19](https://github.com/owid/covid-19-data)
   - **Description**: This dataset provides detailed COVID-19 data on confirmed cases, deaths, and vaccination information by country.
   - **Data Included**:
     - Daily reported cases and deaths
     - Vaccination data by country
     - Demographic data and health indicators

3. **COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University**
   - **Source**: [GitHub Repository - CSSE COVID-19 Data](https://github.com/CSSEGISandData/COVID-19)
   - **Description**: Another source from Johns Hopkins University that provides global case data, including confirmed cases, deaths, and recoveries.
   - **Data Included**:
     - Global case counts
     - Country-level statistics for the spread of COVID-19

### **Key Features of the Dataset**:
- **Confirmed Cases**: The number of COVID-19 confirmed cases reported globally and at the country level.
- **Deaths and Recoveries**: Information on the number of deaths and recoveries due to COVID-19.
- **Vaccination Data**: Global and country-wise vaccination statistics to understand the progress of vaccination campaigns.
- **Time Period**: The data spans from the beginning of the COVID-19 pandemic to the present, with daily updates.


## Folder Structure


The project structure is organized as follows:

```
COVID19_EDA_Project/
├── data/
│   ├── raw/               
│   └── processed/        
├── notebooks/
│   ├── data_cleaning.ipynb   
│   ├── exploratory_analysis.ipynb  
│   └── visualizations.ipynb  
├── dashboard/               
├── reports/
│   └── visuals/            
├── .gitignore               
├── LICENSE                  
├── README.md                
└── requirements.txt    
```     


### Folder Details:
- **`data/raw/`**: Contains the raw datasets that are directly sourced and need processing.
- **`data/processed/`**: Contains cleaned and pre-processed data, ready for analysis.
- **`notebooks/`**: Jupyter notebooks for carrying out the data analysis, cleaning, and visualizations.
- **`dashboard/`**: Contains Dash application files (if you're creating a web-based dashboard for the project).
- **`reports/visuals/`**: This folder stores the saved visualizations (graphs, plots, charts) for reports.
- **`.gitignore`**: Ensures that unnecessary or temporary files are not tracked by Git (such as compiled Python files, logs, or system files).
- **`LICENSE`**: A file that outlines the licensing terms for your project.
- **`README.md`**: The file you are currently reading, which contains project information and guidelines.
- **`requirements.txt`**: Lists the Python libraries that are required to run the project (you can generate this by running `pip freeze > requirements.txt`).



## Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add feature'`).
4. Push your changes to your forked repository (`git push origin feature-branch`).
5. Open a pull request to the `main` branch of the original repository.

Please ensure that your contributions follow the project’s coding style, and add tests/documentation if applicable.

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the data sources used for this project:
  - [Johns Hopkins University COVID-19 Dataset](https://github.com/CSSEGISandData/COVID-19)
  - [Our World in Data COVID-19 Dataset](https://github.com/owid/covid-19-data)
  - [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)

- Thanks to the open-source community for the Python libraries used in this project:
  - `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`, `dash`

- All contributors and collaborators who made this project possible.
