# Introduction

The member should be able to: state and explain steps in a data analysis project; describe objectives, steps, and examples of preparing and wrangling data; describe objectives, methods, and examples of data exploration; describe objectives, steps, and techniques in model training; describe preparing, wrangling, and exploring text-based data for financial forecasting; describe methods for extracting, selecting and engineering features from textual data; evaluate the fit of a machine learning algorithm.

## Summary

Big data—defined as data with volume, velocity, variety, and potentially lower veracity—has tremendous potential for various fintech applications, including several related to investment management., The main steps for traditional ML model building are conceptualization of the problem, data collection, data preparation and wrangling, data exploration, and model training., For textual ML model building, the first four steps differ somewhat from those used in the traditional model: Text problem formulation, text curation, text preparation and wrangling, and text exploration are typically necessary., For structured data, data preparation and wrangling entail data cleansing and data preprocessing. Data cleansing typically involves resolving incompleteness errors, invalidity errors, inaccuracy errors, inconsistency errors, non-uniformity errors, and duplication errors., Preprocessing for structured data typically involves performing the following transformations: extraction, aggregation, filtration, selection, and conversion., Preparation and wrangling text (unstructured) data involves a set of text-specific cleansing and preprocessing tasks. Text cleansing typically involves removing the following: html tags, punctuations, most numbers, and white spaces., Text preprocessing requires performing normalization that involves the following: lowercasing, removing stop words, stemming, lemmatization, creating bag-of-words (BOW) and n-grams, and organizing the BOW and n-grams into a document term matrix (DTM)., Data exploration encompasses exploratory data analysis, feature selection, and feature engineering. Whereas histograms, box plots, and scatterplots are common techniques for exploring structured data, word clouds are an effective way to gain a high-level picture of the composition of textual content. These visualization tools help share knowledge among the team (business subject matter experts, quants, technologists, etc.) to help derive optimal solutions., Feature selection methods used for text data include term frequency, document frequency, chi-square test, and a mutual information measure. Feature engineering for text data includes converting numbers into tokens, creating n-grams, and using name entity recognition and parts of speech to engineer new feature variables., The model training steps (method selection, performance evaluation, and model tuning) often do not differ much for structured versus unstructured data projects., Model selection is governed by the following factors: whether the data project involves labeled data (supervised learning) or unlabeled data (unsupervised learning); the type of data (numerical, continuous, or categorical; text data; image data; speech data; etc.); and the size of the dataset., Model performance evaluation involves error analysis using confusion matrixes, determining receiver operating characteristics, and calculating root mean square error., To carry out an error analysis for each model, a confusion matrix is created; true positives (TPs), true negatives (TNs), false positives (FPs), and false negatives (FNs) are determined. Then, the following performance metrics are calculated: accuracy, F1 score, precision, and recall. The higher the accuracy and F1 score, the better the model performance., To carry out receiver operating characteristic (ROC) analysis, ROC curves and area under the curve (AUC) of various models are calculated and compared. The more convex the ROC curve and the higher the AUC, the better the model performance., Model tuning involves managing the trade-off between model bias error, associated with underfitting, and model variance error, associated with overfitting. A fitting curve of in-sample (training sample) error and out-of-sample (cross-validation sample) error on the y-axis versus model complexity on the x-axis is useful for managing the bias vs. variance error trade-off., In a real-world big data project involving text data analysis for classifying and predicting sentiment of financial text for particular stocks, the text data are transformed into structured data for populating the DTM, which is then used as the input for the ML algorithm., To derive term frequency (TF) at the sentence level and TF–IDF, both of which can be inputs to the DTM, the following frequency measures should be used to create a term frequency measures table: TotalWordsInSentence; TotalWordCount; TermFrequency (Collection Level); WordCountInSentence; SentenceCountWithWord; Document Frequency; and Inverse Document Frequency.

## Learning Outcomes

The member should be able to: state and explain steps in a data analysis project; describe objectives, steps, and examples of preparing and wrangling data; describe objectives, methods, and examples of data exploration; describe objectives, steps, and techniques in model training; describe preparing, wrangling, and exploring text-based data for financial forecasting; describe methods for extracting, selecting and engineering features from textual data; evaluate the fit of a machine learning algorithm.

## Technical Note

**Data Analysis Project Steps**

**Preparing and Wrangling Data**

* **Structured Data:** Cleanse (correct errors) and preprocess (transform) data.
* **Textual Data:** Cleanse (remove tags, punctuation, etc.) and preprocess (normalize, create BOW/n-grams).

**Data Exploration**

* **Structured Data:** Use histograms, box plots, scatterplots for visualization.
* **Textual Data:** Use word clouds to visualize data composition.

**Model Training**

* **Method Selection:** Consider data type, size, and presence of labeled data.
* **Performance Evaluation:** Use confusion matrices, ROC analysis, and error calculation.
* **Model Tuning:** Manage bias and variance errors using fitting curves.

**Preparing Text Data for Financial Forecasting**

* Requires specific cleaning and preprocessing techniques for transforming into structured data.
* Involves extracting features using term frequency and document frequency measures.

**Evaluating Model Fit**

* Use ROC analysis, accuracy, F1 score, precision, and recall to assess performance.
* Consider the trade-off between bias and variance errors during tuning.