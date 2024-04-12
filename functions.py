import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split

# Sampling methods
from imblearn.over_sampling import SMOTE, ADASYN, BorderlineSMOTE, SVMSMOTE
from imblearn.combine import SMOTETomek, SMOTEENN
from imblearn.under_sampling import TomekLinks, RandomUnderSampler

# Algorithms
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier

# Performance metrics
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                            f1_score, roc_auc_score)

import pandas as pd
from IPython.display import Image



# Preprocess the data
def get_preprocessed(df):

    # _MICHD
    #Change 2 to 0 because this means did not have MI or CHD
    df['_MICHD'] = df['_MICHD'].replace({2: 0})


    #1 _RFHYPE6
    #Change 1 to 0 so it represetnts No high blood pressure and 2 to 1 so it represents high blood pressure
    df['_RFHYPE6'] = df['_RFHYPE6'].replace({1:0, 2:1})
    df = df[df._RFHYPE6 != 9]


    #2 TOLDHI3
    # Change 2 to 0 because it is No
    # Remove all 7 (dont knows)
    # Remove all 9 (refused)
    df['TOLDHI3'] = df['TOLDHI3'].replace({2:0})
    df = df[df.TOLDHI3 != 7]
    df = df[df.TOLDHI3 != 9]


    #3 CHOLCHK3
    # Change 1 to 0 and 8 to 0 for Not checked cholesterol in past 5 years
    # Remove 7
    # Remove 9
    df['CHOLCHK3'] = df['CHOLCHK3'].replace({1:0,2:1,3:1,4:1,5:1,6:1,8:0})
    df = df[df.CHOLCHK3 != 7]
    df = df[df.CHOLCHK3 != 9]


    #4 _BMI5 (no changes, just note that these are BMI * 100. So for example a BMI of 4018 is really 40.18)
    df['_BMI5'] = df['_BMI5'].div(100).round(0)


    #5 SMOKE100
    # Change 2 to 0 because it is No
    # Remove all 7 (dont knows)
    # Remove all 9 (refused)
    df['SMOKE100'] = df['SMOKE100'].replace({2:0})
    df = df[df.SMOKE100 != 7]
    df = df[df.SMOKE100 != 9]


    #6 CVDSTRK3
    # Change 2 to 0 because it is No
    # Remove all 7 (dont knows)
    # Remove all 9 (refused)
    df['CVDSTRK3'] = df['CVDSTRK3'].replace({2:0})
    df = df[df.CVDSTRK3 != 7]
    df = df[df.CVDSTRK3 != 9]


    #7 DIABETE4
    # going to make this ordinal. 0 is for no diabetes or only during pregnancy, 1 is for pre-diabetes or borderline diabetes
    # Remove all 7 (dont knows)
    # Remove all 9 (refused)
    df['DIABETE4'] = df['DIABETE4'].replace({2:0, 3:0, 4:1})
    df = df[df.DIABETE4 != 7]
    df = df[df.DIABETE4 != 9]


    #8 _TOTINDA
    # 1 for physical activity
    # change 2 to 0 for no physical activity
    # Remove all 9 (don't know/refused)
    df['_TOTINDA'] = df['_TOTINDA'].replace({2:0})
    df = df[df._TOTINDA != 9]


    #9 _FRTLT1A
    # Change 2 to 0. this means no fruit consumed per day. 1 will mean consumed 1 or more pieces of fruit per day
    # remove all dont knows and missing 9
    df['_FRTLT1A'] = df['_FRTLT1A'].replace({2:0})
    df = df[df._FRTLT1A != 9]


    #10 _VEGLT1A
    # Change 2 to 0. this means no vegetables consumed per day. 1 will mean consumed 1 or more pieces of vegetable per day
    # remove all dont knows and missing 9
    df['_VEGLT1A'] = df['_VEGLT1A'].replace({2:0})
    df = df[df._VEGLT1A != 9]


    #11 _RFDRHV7
    # Change 1 to 0 (1 was no for heavy drinking). change all 2 to 1 (2 was yes for heavy drinking)
    # remove all dont knows and missing 9
    df['_RFDRHV7'] = df['_RFDRHV7'].replace({1:0, 2:1})
    df = df[df._RFDRHV7 != 9]


    #12 _HLTHPLN
    # 1 is yes, change 2 to 0 because it is No health care access
    # remove 9 for don't know or refused
    df['_HLTHPLN'] = df['_HLTHPLN'].replace({2:0})
    df = df[df._HLTHPLN != 9]


    #13 MEDCOST1
    # Change 2 to 0 for no, 1 is already yes
    # remove 7 for don/t know and 9 for refused
    df['MEDCOST1'] = df['MEDCOST1'].replace({2:0})
    df = df[df.MEDCOST1 != 7]
    df = df[df.MEDCOST1 != 9]


    #14 GENHLTH
    # This is an ordinal variable that I want to keep (1 is Excellent -> 5 is Poor)
    # Remove 7 and 9 for don't know and refused
    df = df[df.GENHLTH != 7]
    df = df[df.GENHLTH != 9]


    #15 MENTHLTH
    # already in days so keep that, scale will be 0-30
    # change 88 to 0 because it means none (no bad mental health days)
    # remove 77 and 99 for don't know not sure and refused
    df['MENTHLTH'] = df['MENTHLTH'].replace({88:0})
    df = df[df.MENTHLTH != 77]
    df = df[df.MENTHLTH != 99]


    #16 PHYSHLTH
    # already in days so keep that, scale will be 0-30
    # change 88 to 0 because it means none (no bad mental health days)
    # remove 77 and 99 for don't know not sure and refused
    df['PHYSHLTH'] = df['PHYSHLTH'].replace({88:0})
    df = df[df.PHYSHLTH != 77]
    df = df[df.PHYSHLTH != 99]


    #17 DIFFWALK
    # change 2 to 0 for no. 1 is already yes
    # remove 7 and 9 for don't know not sure and refused
    df['DIFFWALK'] = df['DIFFWALK'].replace({2:0})
    df = df[df.DIFFWALK != 7]
    df = df[df.DIFFWALK != 9]


    #18 _SEX
    # in other words - is respondent male (somewhat arbitrarily chose this change because men are at higher risk for heart disease)
    # change 2 to 0 (female as 0). Male is 1
    df['_SEX'] = df['_SEX'].replace({2:0})


    #19 _AGEG5YR
    # already ordinal. 1 is 18-24 all the way up to 13 wis 80 and older. 5 year increments.
    # remove 14 because it is don't know or missing
    df = df[df._AGEG5YR != 14]


    #20 EDUCA
    # This is already an ordinal variable with 1 being never attended school or kindergarten only up to 6 being college 4 years or more
    # Scale here is 1-6
    # Remove 9 for refused:
    df = df[df.EDUCA != 9]


    #21 INCOME3
    # Variable is already ordinal with 1 being less than $10,000 all the way up to 8 being $75,000 or more
    # Remove 77 and 99 for don't know and refused
    df = df[df.INCOME3 != 77]
    df = df[df.INCOME3 != 99]

    return df


# Get results to a DataFrame
def results_df(resample_method, X_train, X_test, y_train, y_test):

    # Initialize a dictionary to store model names and model objects
    models_dict = {}

    model_names = ['m_lr', 'm_dt', 'm_lgbm', 'm_xgb']
    m_lr = LogisticRegression(random_state=13, class_weight='balanced')
    m_dt = DecisionTreeClassifier(random_state=13, class_weight='balanced')
    m_lgbm = LGBMClassifier(random_state=13, scale_pos_weight=10)
    m_xgb = XGBClassifier(random_state=13, scale_pos_weight=10)


    models = [m_lr, m_dt, m_lgbm, m_xgb]

    tmp = []
    for model, name in zip(models, model_names):
        model.fit(X_train, y_train)  # Train the model
        models_dict[name] = model  # Store the trained model in the dictionary
        
        pred_train = model.predict(X_train)  # Predictions for the training set
        pred_test = model.predict(X_test)  # Predictions for the test set
        
        # Calculate performance metrics
        train_accuracy = accuracy_score(y_train, pred_train)
        precision = precision_score(y_train, pred_train)
        recall = recall_score(y_train, pred_train)
        f1 = f1_score(y_train, pred_train)
        aucc = roc_auc_score(y_train, pred_train)

        acc_test = accuracy_score(y_test, pred_test)
        pre_test = precision_score(y_test, pred_test)
        re_test = recall_score(y_test, pred_test)
        f1_test = f1_score(y_test, pred_test)
        aucc_test = roc_auc_score(y_test, pred_test)

        # Save results to a DataFrame
        tmp.append([resample_method, f'{name}_clf_train', train_accuracy, precision, recall, f1, aucc])
        tmp.append([resample_method, f'{name}_clf_test', acc_test, pre_test, re_test, f1_test, aucc_test])
        tmp.append(['', '', '', '', '', '', ''])

        col_names = ['resampling', 'model_name', 'accuracy', 'precision', 'recall', 'f1', 'roc_auc']
        df = pd.DataFrame(tmp, columns=col_names)

    
    return df
