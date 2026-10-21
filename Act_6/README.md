# Offline Cloud Computing

Durante esta actividad se implementó un flujo de Aprendizaje Federado utilizando el conjunto de datos MNIST.

Se empleó un modelo desarrollado en TensorFlow para el entrenamiento local de cada cliente. La definición de la arquitectura se encuentra en el archivo `model_2.py`.

La partición del conjunto de datos se realizó de forma local y confidencial, fuera del repositorio, dividiendo el dataset en subconjuntos estadísticamente equivalentes y asignando una partición a cada integrante del equipo. El proceso de entrenamiento local se encuentra documentado en el notebook `local_training_2.ipynb`.

Una vez generados los modelos locales (`lmodel_x.keras`), se implementaron y compararon distintas estrategias de agregación federada:

- FedAvg
- FedMedian
- Trimmed Mean

Los resultados obtenidos por cada método fueron comparados entre sí, así como contra un entrenamiento centralizado tradicional. El proceso de agregación y evaluación se encuentra en el notebook `avrg_fed.ipynb`.

Finalmente, cada implementación incluye referencias a los artículos y trabajos de investigación utilizados como base para su desarrollo.


