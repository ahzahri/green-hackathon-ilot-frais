# Business domain glossary

## Google Earth Engine API

- Yacine's feedback: requires a lot of prerequisites before using it.

### `median pixel composite`

In the context of Google Earth Engine API, a median pixel composite is a single image that is created from a collection of images.

### `NVDI`

The Normalized Difference Vegetation Index (NDVI) is a widely used index to measure and monitor plant growth (vegetation) using satellite imagery, including from Landsat satellites. It is based on the observation that different surfaces reflect light differently across different wavelengths.

Specifically, the NDVI makes use of the fact that vegetation absorbs most of the visible light that hits it, and reflects a large portion of the near-infrared light. Non-vegetated features, on the other hand, reflect more visible light and less near-infrared light.

### snippets

Snippets can be run in the Google Earth Engine browser IDE for rapid prototyping => https://code.earthengine.google.com/.

### construct start and end dates for a map

```javascript	
var start = ee.Date('2014-06-01');
var finish = ee.Date('2014-10-01');
```

### get a collection of images based on date and coordinates

```javascript
var filteredCollection = ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
  .filterBounds(point)
  .filterDate(start, finish)
  .sort('CLOUD_COVER', true);
```

#### load, center the map and display it

```javascript
// Load an image.
// catalog of images is available at https://developers.google.com/earth-engine/datasets
var image = ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318');

// Center the map on the image. The 2nd argument is the zoom level.
Map.centerObject(image, 9);

// Display the image.
Map.addLayer(image);
```

#### select a region of interest
    
```javascript
var point = ee.Geometry.Point(-122.262, 37.8719);
```