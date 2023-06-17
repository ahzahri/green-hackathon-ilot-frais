# Green Sight

## Link to the Figma

https://www.figma.com/file/yiXb2m7XGUSfQlANveGIlK/Hackathon?type=design&node-id=0-1&t=qO6tu5IIx5fAEwSC-0

## Projects

### NASA Images fetcher

#### what is this ?

This component is responsible for getting data metadata from geospatial NASA images. To get images, you'll need to input:

- A NASA API key (` X-RateLimit-Limit` response headers shows remaining calls in a rolling hour basis)
- longitude and latitude of the place you want to get images from
- a date for the images

#### prerequisites

- A standard installation of Docker Desktop.
- `ce nasa_images_fetcher && cp .env.example .env` and fill in the missing values in the `.env` file

#### how to use

You can run this component with the following commands:

- `docker compose up -d`
- `docker compose exec nasa-images-fetcher bash -c "python app.py LATITUDE LONGITUDE {DATE}"` (where latitude are longitude are valid coordinates floats and where date begin is optional in the format `YYYY-MM-DD`)
  - if you get no data, try to change the date to a more ancient one with steps of 30 days
- Available imagery bands are:
   - B1: Coastal aerosol
   - B2: Blue
   - B3: Green
   - B4: Red
   - B5: Near Infrared (NIR)
   - B6: Shortwave Infrared (SWIR) 1
   - B7: Shortwave Infrared (SWIR) 2
   - B8: Panchromatic
   - B9: Cirrus
   - B10: Thermal Infrared (TIRS) 1
   - B11: Thermal Infrared (TIRS) 2
- Landsat 8 data has a resolution of 30 meters per pixel for its primary bands

##### GCP stuff

You can authenticate Google Earth Engine API programmatically using a service account. Here's how you can do that:

1. **Create a Google Cloud Project**
   Go to the Google Cloud Console (console.cloud.google.com) and create a new project.
2. **Enable Earth Engine on Your Project**
   Use the Library page in the Cloud Console to enable the Earth Engine API for your project. Also register your project within Earth Engine by visiting the Earth Engine signup page.
3. **Create a Service Account**
   In the Cloud Console, go to the "IAM & Admin -> Service Accounts" page, and create a new service account. Grant it the "Editor" role on your project.
4. **Generate a Key File**
   Generate a new JSON key file for your service account. This file contains the credentials your script will use to authenticate.
5. **Share the Service Account with Earth Engine**
   Share the service account email address with the Earth Engine using the Earth Engine's "Settings" page.
6. **Use the Key File in Your Script**
   In a Python script, you can use the service account key file to authenticate:

   ```python
   import ee

   # Load the service account credentials.
   service_account = 'my-service-account@my-project.iam.gserviceaccount.com'
   credentials = ee.ServiceAccountCredentials(service_account, 'path/to/keyfile.json')

   # Initialize the Earth Engine module.
   ee.Initialize(credentials)
   ```

Replace `'my-service-account@my-project.iam.gserviceaccount.com'` with the email address of your service account, and `'path/to/keyfile.json'` with the path to your service account key file.

Please note that using a service account for authentication is generally recommended for server-to-server API access, not for client applications. Also, keep your service account key file secure and do not expose it in public repositories or websites.

#### NASA Images fetcher TODOs

- expose a REST API to get images
- get better resolution images
- further validation of input args (including env vars)
- endpoint to get latitude and longitude from an address
- save all NASA outputs to a database for further data exploitation and for sparing us a few API key calls
- frontend application to get images with the required input