# Offline Cloud Computing

Durante esta actividad se empleó el modelo de Aprendizaje Federado con el dataset: MNIST
Se empleó un modelo de tensorflow para su entrenamiento el cual se encuentra en (model_2.py)
Posterior se realizó el split del dataset de modo offline y confidencial repartiendo a cada integrante un id con la partición que les correspondía para el entrenamiento, el workflow del mismo se encuentra en (local_training_2.ipynb)
Posteriormente, dados los modelos "lmodel_x.keras", se empleó el FedAvg, FedMedian y Trimmed_mean, comparando los resultados de los mismos al igual que lo que se obtiene de un entrenamiento global centralizado en el notebook (avrg_fed.ipynb)

Así mismo en cada modelo se tiene referencia del paper donde muestra como funcionan estos.