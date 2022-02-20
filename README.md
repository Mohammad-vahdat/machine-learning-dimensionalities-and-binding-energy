# machine-learning-dimensionalities-and-binding-energy



- Generate_labeled_dataframe_including_ASEstructures:

Generate the data frame for labeled structures (based on vdW-DF2)


- MultipleFeaturizer-SHAP: 

This is the main JN that generates the features that is finally used, and also this notebook train the proposed random forest model.

- Adding_BondFractions_BagofBonds_MultipleFeaturizer:

Generate the bag of bonds features and train the corresponding feature.

- Crystal_Graph_Convolutional_Neural_Networks:

Using the crystal graph convolutional NN (cgcnn)

- Featurizer_SiteElementalProperty_AGNIFingerprint_GaussianSymmetryFunction

Testing different featurization technique like site elemental properties, AGNI, and Gaussian symmetry functions

- Regenerate-Fig2C-based-on-ML-model:

Regenerate the figure 2C published in Mounet et al. using the ML trained model.

——

- Featurization_2500_random_structures: 

Generate features for 2500 randomly chosen structures (not necessary the once that passed the LowDimFinder step)

- Test_theModel_on_2500structures:

Use the RF trained model and predict the label for 2500 randomly chosen structures.

- making_set_C-and-featurization:

Extract the structures in Set C (proposed in 2D paper), then making features for all the structures in set C.

- Test_theModel_on_setC:

Test the trained model on structures in set C. 


——

- NewBE-featurizations-BeforeRelaxation:

Make the data frame for all the new structures taken from Davide and featuring them with two different methods.

- NewBE-Testing-BeforeRelaxation:

Predict the label for new structures taken from Davide using the trained ML model

- NewBE-featurizations-AfterRelaxation:

Make the data frame for all the new structures taken from Davide and featuring them with two different methods – AFTER RELAXATION

- NewBE-Testing-AfterRelaxation:

Predict the label for new structures taken from Davide using the trained ML model – AFTER RELAXATION

