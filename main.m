pyrunfile('main.py');
 %opts = detectImportOptions("restaurant1_avg_data.csv");
% %getvaropts(opts,'date');
 %opts = setvaropts(opts,'date','DatetimeFormat','yyyy-MM-dd');
%2015-09-2
%[Date, ItemName, Quantity, ProductPrice, cloud_cover, sunshine, global_radiation, max_temp, mean_temp, min_temp, precipitation, pressure, snow_depth, isPaidTimeOff]= importfile1("restaurant1_data.csv", [2, Inf]);
%restaurant1_data = table(Date, ItemName, Quantity, ProductPrice, cloud_cover, sunshine, global_radiation, max_temp, mean_temp, min_temp, precipitation, pressure, snow_depth, isPaidTimeOff);
restaurant1_data = importfile1("restaurant1_data.csv", [2, Inf]);
%restaurant2_data = importfile1("restaurant2_data.csv", [2, Inf]);

%train model
[trainedModel, validationRMSE] = trainRegressionModel1(restaurant1_data);

%generate prediction
pred = trainedModel.predictFcn(restaurant1_data);


%plot('date', pred, ".")
 plot3(pred, "date", "ItemName")
 grid on