# tickit-predictor
<div id="top"></div>
<!--
*** Thanks for review the tickit-predictor project. If you have any suggestion
*** fork and make a pull request. 
-->

  <h3 align="center">PREDICTOR-README</h3>

  <p align="center">
    A Linear Regression Model based predictor to forecast a number serie that comes from a table of sales. The context is that based on a one month data of entertainment events
  categorized as: shows, music or sports you will predict the quantity of sold tickets for the next seven days after the last row in the feture matrix (X). The predicted (Y) output will be the 
  quantity sold. 
  </p>
  <p> The feature matrix X </p>
  
  ![image](https://user-images.githubusercontent.com/30400445/158910922-52b13652-be28-4419-909b-16af2e987edf.png)

  <p>The predicted output Y or target</p>
  
  ![image](https://user-images.githubusercontent.com/30400445/158911075-289492cf-6edc-48c6-86b2-59b3ed472df2.png)

</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a project forecast based predictions with a Linear Regression model. The project itself is in a basic level, which I will resume in:

  - Load data, train model
  - Implement the Flask library 
  - Deploy to GCP
  - Test the model online

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [pandas](pandas.pydata.org)
* [scikitlearn](https://scikit-learn.org)
* [flask](flask.palletsprojects.com/en/2.0.x/)
* [Bootstrap](https://getbootstrap.com)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The data that you need is in the following link https://dataedo.com/samples/html/Tickit/

### Prerequisites

You will need to use Visual Studio (or some IDE that you like) 
Python 3.9 or 3.7
_Optional: Google Cloud SDK_

### Project Installation


This sections is only for information purpose

1. Open git bash.
2. Create a folder for the project.
3. Clone

   ```sh
   git clone https://github.com/coderunner86/tickit-predictor.git
   ```
4. Go to project root folder with git the command "code ." 
5. This will open Visual Studio code.  After installation, if you look inside you will see a structure like the image below:

* Libraries
* Data
* Templates
* app server
* Model
* Requirements

![image](https://user-images.githubusercontent.com/30400445/158903454-0dfe1c13-c309-410a-ba04-a859ba61c37d.png)

<p align="right">(<a href="#top">back to top</a>)</p>

## Deploy
<!-- Google Cloud SDK -->
_Assuming you have an both project predictor-api and API services enabled, and the SDK installed with the init process started before this step. For more info see: 
https://cloud.google.com/sdk/gcloud/reference/init in order to choose the project that you have in GCP_. 

- Open the cmd, or the linux terminal.
- run command 

 ```sh
   gcloud app deploy --project <project-name>
   ```
 When it's done you will see:
 
 ![image](https://user-images.githubusercontent.com/30400445/158907739-00731450-89ea-4a99-b77b-094ba8c16ecc.png)


- Run command to view your application in the web browser

 ```sh
   gcloud app browse
   ```

<!-- USAGE EXAMPLES -->
## Usage

- Go to the link: 
https://predictor-api-344019.rj.r.appspot.com/

- Click in the predict Button. 

![image](https://user-images.githubusercontent.com/30400445/158905814-e2f1623f-737d-45a5-9469-ee33e2afd9c4.png)

You will be redirected to /predict.html page with predicted quantities for the following seven days afeter the last row in the data used for the feature matrix.

![image](https://user-images.githubusercontent.com/30400445/158905883-ec42b8d7-87f7-475e-8f26-8e4b6ff49ea2.png)


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Improve the architecture with best practices https://cloud.google.com/architecture/ml-on-gcp-best-practices
- [ ] Search for a better model performance.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

[Jesus Legarda](https://www.linkedin.com/in/coderunner86/) - java@unicauca.edu.co

Project Link: https://github.com/coderunner86/tickit-predictor

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I like to give credit to:

* https://medium.com/@nutanbhogendrasharma


<p align="right">(<a href="#top">back to top</a>)</p>

