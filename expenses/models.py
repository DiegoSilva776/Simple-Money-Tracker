# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from decimal import Decimal

class Expense(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    value = models.DecimalField(0, max_digits=20, decimal_places=2)
    category = models.TextField()
    highlighted = models.TextField()

    # Relationships
    owner = models.ForeignKey('auth.User', related_name='expenses', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Always make the first letter of the title uppercase
        """
        # Modify the title appearance
        self.title = self.title.capitalize()

        # Create a highlighted version of the object
        self.highlighted = 'Despesa %s : %f' % (self.title, self.value)



        # Create new endpoint to return the expenses by classification
        print("Running a supervisioned learning algorithm to extrac the category of the input, via classification ...")
        print("1 - Collecting data [features, labels] to train the classifier ...")
        print("2 - Training the classifier ...")
        print("3 - Making a prediction of the expense category ...")
        print("4 - We got a category (:")

        '''
        from sklearn import tree
        features = [[140,1], [130,1], [150,0], [170,0]]
        labels = [0, 0, 1, 1]
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(features, labels)
        print (clf.predict([[150, 0]]))

        # Add the predicted category to the new object, based on its description
        self.category = clf.predict([[150, 0]])
        '''

        
        # Use a LinearModel to perform text categorization
        print('Using a LinearModel to perform text categorization ...')
        categories = [
            'transporte',
            'saude', 
            'supermercado', 
            'hortifruti', 
            'padaria', 
            'acougue', 
            'telefone',
            'agua_potavel',
            'luz',
            'agua',
            'internet',
            'aluguel',
            'gas',
            'roupas',
            'sophia_bebe',
            'educacao',
            'lazer',
            'itens_casa'
        ]

        # Load the target_names
        print('Loading the target_names ...')
        twenty_train = dict()
        twenty_train['target_names'] = categories
        print(twenty_train['target_names'])

        # Load the data of each text file
        print('Loading the data of each text file ...')
        twenty_train['data'] = [
            'transporte, passagens de ônibus, passagem de ônibus, táxi, táxis, bicileta, bicicletas, uber, ubers',
            'saúde, farmácia, remédio, remédios, hospital',
            'supermercado, super mercado, compras do mês, compras, feira, arroz, refrigerante, coca-cola, coca, fanta, guaraná, feijão macarrão, miojo, rámen, mostarda, maionese',
            'hortifruti, verduras, legumes, frutas',
            'padaria, leite, pão, pao, bolo, saco de pão, pão francês, pães franceses, biscoito, biscoitos, bolacha, bolachas, rosca, bolo, bolo de rôlo, tapioca',
            'açougue, acougue, carne, frango, galeto, bife, vaca, carne de vaca, carne moída, carne guizada, guizado, carne cozida',
            'telefone, créditos para o celular, celular, créditos tim, créditos vivo, crétidos claro, créditos oi',
            'água potável, agua potavel, galão de água, seu iran, sr. iran, água, agua',
            'luz, conta de luz, eletricidade, energia eletrica, energia elétrica',
            'água, agua, conta de água',
            'internet, conta de internet, conta da vivo',
            'aluguel, aluguel do apartamento, apartamento, sr. fernando, seu fernando',
            'gás, gas, conta de gás',
            'roupa, roupas, blusa, camisa, camiseta, calça, meia, cueca, calcinha, saia, vestido, blusa blusinha, vestido, chinela, chinelo, sapato, tênis, sandália, rasteirinha, body, biquini, sutiã, maiô, sunga, bermuda, shorts',
            'fralda, fraldas, leite em pó, ninho, sacos de leite em pó, lenço umedecido, lenços umedecidos, lenço humidecido, lenços humidecidos, cotonete, cotonetes, algodão, sacos de algodão',
            'educação, educacao, livro, revista, veja, curso, tutorial',
            'netflix, passeio, saída, praia, aniversário',
            'capa de sofá, sofá, cortina, tapete, estante, armário, cama, escrivaninha, mesa, guarda-roupas, guarda roupas, rack, raque, geladeira, máquina de lavar, máquina, tv, fogão, cadeira, cadeiras'
        ]
        print(twenty_train['data'][0])

        # Load the target of each data row
        print('Loading the target of each data row ...')
        twenty_train['target_names'] = [
            'transporte',
            'saude', 
            'supermercado', 
            'hortifruti', 
            'padaria', 
            'acougue', 
            'telefone',
            'agua_potavel',
            'luz',
            'agua',
            'internet',
            'aluguel',
            'gas',
            'roupas',
            'sophia_bebe',
            'educacao',
            'lazer',
            'itens_casa'
        ]
        print(twenty_train['target_names'])

        # Load the target of each data row as integers
        print('Loading the target of each data row as integers ...')
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
            16,
            17
        ]
        print(twenty_train['target'])

        # Recover the target label of each data row with the target index value
        print('Recovering the target label of each data row with the target index value ...')
        for t in twenty_train['target'][:len(twenty_train['target'])]:
            print(twenty_train['target_names'][t])


        # Create vectors in the format 'Bag of words' for each training instance of the training set
        print('Creating vectors in the format \'Bag of words\' for each training instance of the training set ...')
        from sklearn.feature_extraction.text import CountVectorizer
        count_vect = CountVectorizer()

        X_train_counts = count_vect.fit_transform(twenty_train['data'])
        print(X_train_counts.shape)

        # Frequency of the word refrigerante
        #print('Frequency of the word refrigerante')
        #print(count_vect.vocabulary_.get(u'refrigerante'))
        #print(X_train_counts[count_vect.vocabulary_.get(u'refrigerante')])

        # Transforming word occurrencies in frequencies
        print('Transforming word occurrencies in frequencies ...')
        from sklearn.feature_extraction.text import TfidfTransformer
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        print(X_train_tfidf.shape)

        # Training a classifier
        print('Training a classifier with the NaiveBayes algorithm ...')
        from sklearn.naive_bayes import MultinomialNB
        clf = MultinomialNB().fit(X_train_tfidf, twenty_train['target'])

        docs_new = [self.title]
        X_new_counts = count_vect.transform(docs_new)
        X_new_tfidf = tfidf_transformer.transform(X_new_counts)

        predicted = clf.predict(X_new_tfidf)

        for doc, category in zip(docs_new, predicted):
            print('%r => %s' % (doc, twenty_train['target_names'][category]))        


        super(Expense, self).save(*args, **kwargs)
