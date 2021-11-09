FROM python:3

ADD JAucamp_factorial_digits.py .

CMD [ "python", "./JAucamp_factorial_digits.py" ]

ENTRYPOINT ["python","./JAucamp_factorial_digits.py"]