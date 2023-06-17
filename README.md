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

#### NASA Images fetcher TODOs

- further validation of input args (including env vars)
- endpoint to get latitude and longitude from an address
- save all NASA outputs to a database for further data exploitation and for sparing us a few API key calls
- frontend application to get images with the required input