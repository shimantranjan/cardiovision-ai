# CardioVision AI — Dataset Research

## Research Objective

Identify retinal fundus image datasets that contain sufficient cardiovascular information to support scientifically valid cardiovascular risk prediction.

## Primary Prediction Target

10-year cardiovascular / ASCVD risk.

## Secondary Targets

- Systolic blood pressure
- Age
- Smoking status
- Cardiovascular risk factors
- Major adverse cardiovascular events (if appropriate labels are available)

## Candidate Dataset

UK Biobank retinal fundus imaging.

## External Validation Candidate

EyePACS 10K.

## Key Requirements

A usable dataset should provide:

1. Retinal fundus images
2. Patient-level identifiers
3. Cardiovascular or risk-related labels
4. Relevant demographic/clinical variables
5. Sufficient sample size
6. Appropriate data access rights

## Important Research Constraint

We must split data at the patient level rather than the image level to prevent data leakage when multiple retinal images belong to the same participant.

## Project Principle

We will not relabel an ophthalmic disease dataset as cardiovascular data.

## Status

Dataset research — in progress.