# Ebrains Atlascore python library 

This library is a wrapper for the [ebrains atlascore](https://ebrains-atlascore.apps.hbp.eu/) REST API

Author: Vadim Marcenko

## Installation

`pip install ebrains-atlascore`

## Basic setup

The library is using the latest production version of the Atlascore API.
If you want to use a development version you have to set it as an environment variable:

`export ATLAS_CORE_ENV=DEV`

## Basic Usage with examples

Get all referencespaces known by the atlas-core:

`referencespaces.get_all_referencespaces()`

Get a single referencespace by a given name:

`referencespaces.get_referencespace_by_name('colin')`

Get all parcellations for a referencespace name:

`parcellations.get_all_parcellations('colin')`

Get a single parcellation for a reference name:

`parcellations.get_parcellation_by_name('colin', 'JuBrain Cytoarchitectonic Atlas')`

Get all regions for a parcellation in a referencespace:

`regions.get_all_regions('colin', 'JuBrain Cytoarchitectonic Atlas')`

Get a single region for a parcellation in a referencespace:

`regions.get_region_by_name('colin', 'JuBrain Cytoarchitectonic Atlas', 'Area Fp1 (FPole) - left hemisphere)`

Retrieve a probability map for a region as a ROI:

`regions.get_probability_map_for_region(Region('Area_Fp1', 'colin', 'JuBrain Cytoarchitectonic Atlas'), Hemisphere.LEFT.value, 0.2)`
