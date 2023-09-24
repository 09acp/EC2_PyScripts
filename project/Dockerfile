FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
# ADD main.py /
ADD feature_eng.py / InputData.db / OutputData.db /
# CMD [ "python", "./main.py" ]
CMD [ "python", "./feature_eng.py" ]
