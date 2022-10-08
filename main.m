pyrunfile('main.py');

restaurant1_data = importfile1("restaurant1_data.csv", [2, Inf]);
restaurant2_data = importfile1("restaurant2_data.csv", [2, Inf]);

%[trainedModel, validationRMSE] = trainRegressionModel(restaurant1_data)
[trainedModel, validationRMSE] = trainRegressionModel1(restaurant1_data);

%generate prediction
pred = trainedModel.predictFcn(restaurant1_data);

plot3('Item Name', 'date', pred, ".")
grid on