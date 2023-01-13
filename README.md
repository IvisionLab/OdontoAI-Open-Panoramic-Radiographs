# Boosting research on dental panoramic radiographs: A challenging data set, baselines, and a task-central online platform for benchmark
In this repo, you will find the instructions on how to [request the data set](#Request-the-Data-Set), soon-to-be published and used to perform the experiments of the aforementioned paper.
We started from the [DNS Panoramic Images v2 data set](https://github.com/IvisionLab/dns-panoramic-images-v2), which comprises 450 panoramic dental radiographs.
The initial data set was used for benchmarking the performance of several instance segmentation networks, and the winner architecture was used to speed up the annotation process through the Human-in-the-Loop (HITL) concept.
We consider that this new data set evolves all of our previously published data sets: [UFBA UESC DENTAL IMAGES](https://github.com/IvisionLab/dental-image), [UFBA UESC DENTAL IMAGES **Deep**](https://github.com/IvisionLab/deep-dental-image), [DNS Panoramic Images](https://github.com/IvisionLab/dns-panoramic-images), [DNS Panoramic Images v2](https://github.com/IvisionLab/dns-panoramic-images).
Therefore, we deprecated all previously published data sets in favor of this new one called **OdontoAI Open Panoramic Radiographs**.
To be notified of code releases, new data sets, and errata, watch this repo.

## Data set statistics
The data set comprises 4000 panoramic images, from which 850 were manually labeled from scratch, and the 3150 remaining others were annotated using the Human-in-The-Loop concept.
We only release the annotations of 2000 radiographs (650 from scratch and 1350 using HITL), while the other 2000 are used for model evaluation at our platform, called OdontoAI.
The table below summarizes the data used according to image categories.
These categories group the images according to the presence of 32 teeth, restoration, and dental appliances, revealing the high variability of the images.
Categories 5 and 6 are reserved for patients with dental implants and more than 32 teeth, respectively.

| Category |      32 Teeth      |     Restoration    |      Appliance     | Number and Inst. Segm. |
|:--------:|:------------------:|:------------------:|:------------------:|:----------------------:|
|     1    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |            93          |
|     2    | :heavy_check_mark: | :heavy_check_mark: |                    |           438          |
|     3    | :heavy_check_mark: |                    | :heavy_check_mark: |           110          |
|     4    | :heavy_check_mark: |                    |                    |           274          |
|     5    |                    |      Implants      |                    |           228          |
|     6    |                    | More than 32 teeth |                    |           335          |
|     7    |                    | :heavy_check_mark: | :heavy_check_mark: |           420          |
|     8    |                    | :heavy_check_mark: |                    |          1804          |
|     9    |                    |                    | :heavy_check_mark: |            93          |
|    10    |                    |                    |                    |           205          |
|          |                    |                    |        Total       |          4000          |

## Citation
If you use this data set, our paper (**[OdontoAI Open Panoramic Radiographs](https://https://arxiv.org/abs/2203.15856)**) should be cited.):

B. Silva, L. Pinheiro, B. Sobrinho, F. Lima, B. Sobrinho, K. Abdalla, M. Pithon, P. Cury, and L. Oliveira, “OdontoAI: A human-in-the-loop labeled data set and an online platform to boost research on dental panoramic radiographs,” in arXiv, 2022.

```
<!---
@article{silva2022odontoai,
  title={OdontoAI: A human-in-the-loop labeled data set and an online platform to boost research on dental panoramic radiographs},
  author={Silva, Bernardo and Pinheiro, La{\'\i}s and Sobrinho, Brenda and Lima, Fernanda and Sobrinho, Bruna and Abdalla, Kalyf and Pithon, Matheus and Cury, Patr{\'\i}cia and Oliveira, Luciano},
  journal={arXiv preprint arXiv:2203.15856},
  year={2022}
} 
--->

@article{doi:10.1080/21681163.2022.2157747,
author = {Bernardo Peters Menezes Silva and Laís Bastos Pinheiro and Brenda Pereira Pinheiro Sobrinho and Fernanda Pereira Lima and Bruna Pereira Pinheiro Sobrinho and Kalyf Abdalla Buzar Lima and Matheus Melo Pithon and Patricia Ramos Cury and Luciano Rebouças de Oliveira},
title = {Boosting research on dental panoramic radiographs: a challenging data set, baselines, and a task central online platform for benchmark},
journal = {Computer Methods in Biomechanics and Biomedical Engineering: Imaging \& Visualization},
volume = {0},
number = {0},
pages = {1-21},
year  = {2023},
publisher = {Taylor & Francis},
doi = {10.1080/21681163.2022.2157747}}

```

## Previous Works
This data set and its corresponding paper are a continuation of other works of our group.
Please, consider reading and citing:

- B. Silva, L. Pinheiro, L. Oliveira, and M. Pithon, “A study on tooth segmentation and numbering using end-to-end deep neural networks,” in Conference on Graphics, Patterns and Images. IEEE, 2020.

```
@inproceedings{silva2020study,
  title={A study on tooth segmentation and numbering using end-to-end deep neural networks},
  author={Silva, Bernardo and Pinheiro, La{\'\i}s and Oliveira, Luciano and Pithon, Matheus},
  booktitle={Conference on Graphics, Patterns and Images (SIBGRAPI)},
  year={2020},
  organization={IEEE}
}
```

- G. Jader, J. Fontineli, M. Ruiz, K. Abdalla, M. Pithon, and L. Oliveira, “Deep instance segmentation of teeth in panoramic X-ray images,” in Conference on Graphics, Patterns and Images. IEEE, 2018.
```
@inproceedings{jader2018deep,
  title={Deep instance segmentation of teeth in panoramic X-ray images},
  author={Jader, Gil and Fontineli, Jefferson and Ruiz, Marco and Abdalla, Kalyf and Pithon, Matheus and Oliveira, Luciano},
  booktitle={Conference on Graphics, Patterns and Images (SIBGRAPI)},
  pages={400--407},
  year={2018},
  organization={IEEE}
}
```

- G. Silva, L. Oliveira, and M. Pithon, “Automatic segmenting teeth in X-ray images: Trends, a novel data set, benchmarking and future perspectives,” Expert Systems with Applications, Patterns and Images. vol. 107, pp. 15-31, 2018.
```
@article{silva2018automatic,
  title={Automatic segmenting teeth in X-ray images: Trends, a novel data set, benchmarking and future perspectives},
  author={Silva, Gil and Oliveira, Luciano and Pithon, Matheus},
  journal={Expert Systems with Applications},
  volume={107},
  pages={15--31},
  year={2018},
  publisher={Elsevier}
}
```

- L. Pinheiro, B. Silva, B. Sobrinho, F. Lima, P. Cury, L. Oliveira, “Numbering permanent and deciduous teeth via deep instance segmentation in panoramic X-rays,” in Symposium on Medical Information Processing and Analysis (SIPAIM). SPIE, 2021.
```
@inproceedings{pinheiro2021numbering,
  title={Numbering permanent and deciduous teeth via deep instance segmentation in panoramic X-rays},
  author={Pinheiro, La{\'\i}s and Silva, Bernardo and Sobrinho, Brenda and Lima, Fernanda and Cury, Patr{\'\i}cia and Oliveira, Luciano.},
  booktitle={Symposium on Medical Information Processing and Analysis (SIPAIM)},
  year={2021},
  organization={SPIE}
}
```

## Demonstration
Follow the provided jupyter notebook demo.ipynb to get a quick sense of the data set.
The conversions.py file defines useful functions to visualize the annotations.

<!---- 
## Request the Data Set
Copy the text below in a PDF file, fill out the fields in the text header, and sign it at the end. Please send an e-mail to lrebouca@ufba.br to receive a link to download the **OdontoAI Open Panoramic Radiographs** data set with the PDF in attachment. The e-mail must be sent from a professor's valid institutional account:


**Subject**: Request to download the OdontoAI Open Panoramic Radiographs.

"Name: [your first and last name]

Affiliation: [university where you work]

Department: [your department]

Current position: [your job title]

E-mail: [must be the e-mail at the above-mentioned institution]

I have read and agreed to follow the terms and conditions below: The following conditions define the use of the OdontoAI Open Panoramic Radiographs:

This data set is provided "AS IS" without any express or implied warranty. Although every effort has been made to ensure accuracy, IvisionLab does not take any responsibility for errors or omissions;

Without the expressed permission of IvisionLab, any of the following will be considered illegal: redistribution, modification, and commercial usage of this data set in any way or form, either partially or in its entirety;

All images in this data set are only allowed for demonstration in academic publications and presentations;

This data set will only be used for research purposes. I will not make any part of this data set available to a third party. I'll not sell any part of this data set or make any profit from its use.

[your signature]"  

**P.S. A link to the data set file will be sent as soon as possible.** --->
