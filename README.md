# Singapore Tourism Board Open API

# Table of Contents


---
# 1. Introduction
In 2019 the Covid pandemic forced the global tourism industry into slowdown. During this period tourism related businesses had to "go digital" to offer unique tour experiences and employ digital marketing to reach their target audience. Fast forward to 2023, tourism related businesses are now more digitally savvy and better able to take advantage of the digital substrate.

To increase productivity and to enhance the information transparency for all tourist visiting Singapore. The Singapore Tourism Board has in 2022 unveiled their Tourism Information & Services Hub (TIH). TIH serves as a one stop shop to access tourism related offerings and travel software services in Singapore.

In this project, I show case the content user api


## 1.1 Open API's by Singapore Tourism Board

- Register for an api key [here](https://tih-iam.stb.gov.sg/iamsso/register?service=https://tih.stb.gov.sg/bin/loginValidation&regType=dev)
- Review user related content [here](https://tih-dev.stb.gov.sg/content-api/apis)

---
# 2. Application Deployment and Folder Structure

The entire file system was created in a virtual environment using conda, using python 3.9. Please follow the following steps to deploy application.
## 2.1 Application deployment
1. Create conda environment and activate it using:
    ```bash
    conda create --name sgtih python=3.9
    conda activate sgtih
    ```
2. Install dependencies using:
    ```bash
    pip install -r requirements.txt
    ```
3. Create a .env file and input registered api key under 'apikey', you can register for an api key [here](https://tih-iam.stb.gov.sg/iamsso/register?service=https://tih.stb.gov.sg/bin/loginValidation&regType=dev).
   ```bash
   touch .env
   echo API_KEY = 'apikey' > .env
   ```


## 2.2 Folder directory

The folder directory layout is as below:
```bash
```

---
# 3. Data Ingestion Pipeline

```mermaid
graph LR;
    A-->B;
    A-->C;
    B-->E;
    C-->E;
    E-->D;
```
# 4. 
