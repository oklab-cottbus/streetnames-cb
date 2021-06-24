library(tidyverse)
library(osmdata)
library(sf)
library(gdalUtils)
library(rgdal)
library(maptools)
library(raster)

cbs<-getbb("Cottbus Germany")

#### getosmdata
streets <- getbb("Cottbus Germany") %>%
  opq() %>%
  add_osm_feature(key = "highway", 
                  value = c("motorway", "primary", 
                            "secondary", "tertiary",
                            "residential", "living_street",
                            "unclassified",
                            "service", "footway")) %>%
  osmdata_sf()

dsn <- "WFS:https://cardo.cottbus.de/net3/public/ogc.ashx?NodeId=75&Service=WFS&Request=GetCapabilities&"
ogrinfo(dsn, so=TRUE)
ogr2ogr(dsn, "L60.shp", "L60")

cb <- readOGR("L60.shp", "L60", stringsAsFactors=FALSE)
#plot(cb)

#writeSpatialShape(cb, "cb", proj4string=crs(cb))
#cb_shp <- readOGR("cb.shp", stringsAsFactors=FALSE)

#### crs transform
cb_4326 <-st_as_sf(cb) %>% st_transform(., crs = 4326)

#### subsets streets per district
s_per_q<-lapply(cb_4326$geometry, function(x) {streets$osm_lines[x,] })
names(s_per_q)<-cb_4326$name

#### controll-plot
#plot(cb_4326$geometry)
#sapply(s_per_q, function(x){
#  Sys.sleep(1)
#  plot(x, add=T)
#})

#### namelist
namelist<-sapply(s_per_q, function(x) 
  x$name[!is.na(x$name)] %>% unique(.) 
)

lapply(namelist, write, "names-cottbus.csv", append=TRUE, ncolumns=1)
