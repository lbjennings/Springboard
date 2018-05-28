########
#build Dockerfile
#####
FROM  jupyter/pyspark-notebook 
 
LABEL maintainer="lucas.b.jennings@gmail.com"

WORKDIR /app

RUN conda install jupyter -y && \
    conda install pandas -y && \
    conda clean -y -all


EXPOSE 8888

VOLUME /app

CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
