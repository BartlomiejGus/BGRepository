%HDLC
%clear all;

%Below for HDLC controller
mse = 1*10^(-16); % Target error MSE
S = 3; %Number of inputs
K = 10; %Number of neurons in I layer
R = 5; %Number of neurons in II layer
W = 1; %Number of neurons in III layer output
weigths_W1 = rand ( S+1 , K ) * 0.2 - 0.1; %Weights of I layer
weights_W2 = rand ( K+1 , R ) * 0.2 - 0.1; %Weights of II layer
weights_W3 = rand ( R+1 , W ) * 0.2 - 0.1; %Weights of III layer


%Below for DRNN model

S = 3; %Liczba wejsc do sieci
K = 10; %Liczba neuronow w warstwie ukrytej
W = 1; %Liczba neuronow w warstwie wyjsciowej
weights_W1_model = rand ( S  , K ) * 0.2 - 0.1;
weights_W2_model = rand ( K , W ) * 0.2 - 0.1;
weights_Wd_model = rand (K,1)* 0.2 - 0.1;
weights_Xj_model = rand (K,1)* 0.2 - 0.1;
previous_input_to_hidden_layer = rand (K,1)* 0.2 - 0.1;
weights_Y1_model = rand (K,1)* 0.2 - 0.1;
weights_Qj_model = rand (S,K)* 0.2 - 0.1;
