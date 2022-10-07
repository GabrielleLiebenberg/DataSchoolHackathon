pyrunfile('main.py');

restaurant1_data = importfile1("restaurant1_data.csv", [2, Inf]);
restaurant2_data = importfile1("restaurant2_data.csv", [2, Inf]);
%restaurant1_data = pyrunfile('main.py', 'restaurant1_complete');
%restaurant2_data = pyrunfile('main.py', 'restaurant2_complete');
%restaurant1_data = restaurant1_data.toTable();
