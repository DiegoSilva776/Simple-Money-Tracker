# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from decimal import Decimal

class Expense(models.Model):
    # Attributes
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    value = models.DecimalField(0, max_digits=20, decimal_places=2)
    category = models.TextField()
    highlighted = models.TextField()

    # Relationships
    owner = models.ForeignKey('auth.User', related_name='expenses', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('created',)

    # Functions
    def save(self, *args, **kwargs):
        # Modify the title appearance
        self.title = self.title.capitalize()

        # Create a highlighted version of the object
        self.highlighted = 'Despesa %s : %f' % (self.title, self.value)

        # Get the category of the expense based on a Machine Learning algorithm that 
        # predicts the value based on the expense title
        self.category = self.getCategoryFromMachineLearning(self.title)

        super(Expense, self).save(*args, **kwargs)

    '''
        Create new endpoint to return the expenses by classification
        Reference:
        http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
        http://scikit-learn.org/stable/auto_examples/text/document_classification_20newsgroups.html
    '''
    def getCategoryFromMachineLearning(self, title):
        print("\n\nRunning a supervisioned learning algorithm to extrac the category of the input, via classification ...")
        
        # Use a LinearModel to perform text categorization
        print('\n1 - Using a LinearModel to perform text categorization ...')
        categories = [
            'bebê',
            'padaria', 
            'acougue', 
            'roupas',
            'água',
            'educacao',
            'luz',
            'gas',
            'hortifruti', 
            'saude', 
            'casa',
            'aluguel',
            'internet',
            'telefone',
            'lazer',
            'supermercado', 
            'transporte'
        ]

        # Load the target_names
        print('\n2 - Loading the target_names ...')
        twenty_train = dict()
        twenty_train['target_names'] = categories
        print(twenty_train['target_names'])

        # Load the data of each text file
        print('\n3 - Loading data to train the Classification algorithm with content relevant to each category ...')
        
        # Load the text related to each category, this text is going to be vectorized later into a bag 
        # of words in order to make it possible to train the classifier
        import os
        from money_monitor.settings import BASE_DIR
        
        twenty_train['data'] = []
        datasetFileNames = [
            'cat_baby_care.txt',
            'cat_bakery.txt',
            'cat_butchery.txt',
            'cat_clothes.txt',
            'cat_water.txt',
            'cat_education.txt',
            'cat_energy.txt',
            'cat_gas.txt',
            'cat_greenery.txt',
            'cat_health.txt',
            'cat_house_items.txt',
            'cat_house_rent.txt',
            'cat_internet.txt',
            'cat_phone.txt',
            'cat_recreation.txt',
            'cat_supermarket.txt',
            'cat_transport.txt'
        ]

        # Fill the training data with texts that reflect each one of the categories
        for filename in datasetFileNames:
            print('Loading content from file: ' + filename + ' ...')

            with open(os.path.join(BASE_DIR, 'machine_learning_datasets/' + filename), 'r') as myfile:
                fileContent = myfile.read()
                twenty_train['data'].append(fileContent)
                
        # Load the target of each data row
        print('\n4 - Loading the target of each data row ...')
        twenty_train['target_names'] = [
            'bebê',
            'padaria', 
            'acougue', 
            'roupas',
            'água',
            'educacao',
            'luz',
            'gas',
            'hortifruti', 
            'saude', 
            'casa',
            'aluguel',
            'internet',
            'telefone',
            'lazer',
            'supermercado', 
            'transporte'
        ]
        print(twenty_train['target_names'])

        # Load the target of each data row as integers
        print('\n5 - Loading the target of each data row as integers ...')
        twenty_train['target'] = [
            0,
            1, 
            2, 
            3, 
            4, 
            5, 
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16
        ]
        print(twenty_train['target'])

        # Recover the target label of each data row with the target index value
        print('\n6 - Recovering the target label of each data row with the target index value ...')
        for t in twenty_train['target'][:len(twenty_train['target'])]:
            print(twenty_train['target_names'][t])

        # Manually building a Pipeline with a CountVectorizer -> TfidfTransformer -> Classifier
        print('Manually building a Pipeline with a CountVectorizer -> TfidfTransformer -> Classifier ...')

        # Create vectors in the format 'Bag of words' for each training instance of the training set
        print('\n7 - Creating vectors in the format \'Bag of words\' for each training instance of the training set ...')
        from sklearn.feature_extraction.text import CountVectorizer
        count_vect = CountVectorizer()

        X_train_counts = count_vect.fit_transform(twenty_train['data'])
        print(X_train_counts.shape)

        # Transforming word occurrencies in frequencies
        print('\n8 - Transforming word occurrencies in frequencies ...')
        from sklearn.feature_extraction.text import TfidfTransformer
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        print(X_train_tfidf.shape)

        # Training a classifier
        print('\n9 - Training a classifier with the NaiveBayes algorithm ...')
        #  NaiveBayes: precision 0.705882352941
        from sklearn.naive_bayes import MultinomialNB
        clf = MultinomialNB()
        clf.fit(X_train_tfidf, twenty_train['target'])

        # Support Vector Machine: precision 0.5882 
        # from sklearn.linear_model import SGDClassifier
        # clf = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None)
        # clf.fit(X_train_tfidf, twenty_train['target'])

        # Evaluating the performance of the classifier with a test set
        print('\n10 - Evaluating the performance of the prediction algorithm for the test set ...')
        import numpy as np
        twenty_test = dict()
        twenty_test['target'] = twenty_train['target']
        docs_test = [
            'mamadeira',
            'bolo de rolo', 
            'carne', 
            'camiseta',
            'conta de água',
            'lápis',
            'conta de luz',
            'conta de gás',
            'verduras & frutas', 
            'farmácia', 
            'tapete',
            'aluguel',
            'internet',
            'telefone',
            'passeio',
            'feira do mês', 
            'VEM'
        ]

        docs_new = docs_test
        X_new_counts = count_vect.transform(docs_new)
        X_new_tfidf = tfidf_transformer.transform(X_new_counts)

        predicted = clf.predict(X_new_tfidf)
        print(np.mean(predicted == twenty_test['target']))

        # Make predictions for the expense category, based on the trained classifier
        print('\n11 - Making predictions for the expense category, based on the trained classifier ...')
        docs_new = [title]
        X_new_counts = count_vect.transform(docs_new)
        X_new_tfidf = tfidf_transformer.transform(X_new_counts)

        predicted = clf.predict(X_new_tfidf)
        predictedCategory = ''
        
        for doc, category in zip(docs_new, predicted):
            predictedCategory =  twenty_train['target_names'][category]
            print('%r => %s' % (doc, predictedCategory))

        # Print final message
        print("\nDone predicting category for new expense.")

        return predictedCategory
