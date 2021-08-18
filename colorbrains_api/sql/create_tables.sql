--docker run -d --name mycontainer -p 80:80 myimage
--psql -h localhost -U colorbrains -W colorbrains

-- create schema for mpl
CREATE SCHEMA IF NOT EXISTS matplotlib;


-- create table for basecolors
CREATE TABLE IF NOT EXISTS matplotlib.basecolors (
    color_name VARCHAR[1] PRIMARY KEY,
    red FLOAT NOT NULL CHECK (red >= 0 AND red <=1),
    green FLOAT NOT NULL CHECK (green >= 0 AND green <=1),
    blue FLOAT NOT NULL CHECK (blue >= 0 AND blue <=1)
);


-- create table for reference `color category` -> `colormap`
-- effectively labeled data
-- if a colormap has 22 colors `cmap_n_total` will be 22 
CREATE TABLE IF NOT EXISTS matplotlib.categorizedcolormaps (
    categorical_name VARCHAR[30] UNIQUE NOT NULL PRIMARY KEY,
    colormap_name VARCHAR[20] UNIQUE NOT NULL,
    cmap_n_total INT NOT NULL
);


-- create table for colormaps
-- if a colormap has 22 colors `cmap_n_total` will be 22 
-- cmap_n_observation will be 1..22
-- references above table: matplotlib.categorizedcolormaps
CREATE TABLE IF NOT EXISTS matplotlib.colormaps (
    colormap_name VARCHAR[20] NOT NULL,
    
    cmap_n_observation INT NOT NULL, 

    red FLOAT NOT NULL CHECK (red >= 0 AND red <=1),
    green FLOAT NOT NULL CHECK (green >= 0 AND green <=1),
    blue FLOAT NOT NULL CHECK (blue >= 0 AND blue <=1),
    
    PRIMARY KEY (colormap_name, cmap_n_observation),
    FOREIGN KEY (colormap_name) REFERENCES matplotlib.categorizedcolormaps (colormap_name)
);


-- create table for named colors
CREATE TABLE IF NOT EXISTS matplotlib.namedcolors (
    color_name varchar[20] NOT NULL PRIMARY KEY,
    red float NOT NULL CHECK (red >= 0 AND red <=1),
    green float NOT NULL CHECK (green >= 0 AND green <=1),
    blue float NOT NULL CHECK (blue >= 0 AND blue <=1)
);
