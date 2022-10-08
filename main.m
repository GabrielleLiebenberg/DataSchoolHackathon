pyrunfile('main.py');
 %opts = detectImportOptions("restaurant1_avg_data.csv");
% %getvaropts(opts,'date');
 %opts = setvaropts(opts,'date','DatetimeFormat','yyyy-MM-dd');
%2015-09-2

restaurant1_data = importfileAVG("restaurant1_avg_data.csv", [2, Inf]);
restaurant2_data = importfileAVG("restaurant2_avg_data.csv", [2, Inf]);

%train model
%[trainedModel, validationRMSE] = trainRegressionModel1(restaurant1_data);

%generate prediction
%pred = trainedModel.predictFcn(restaurant1_data);

% plot3('Item Name', 'date', pred, ".")
% grid on