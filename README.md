# Если вы читаете это сообщение, то проект пока не нашёл своего завершения (или даже mvp). Отложите, пожалуйста, его проверку в пользу других проектов. Достойный проверки результат будет закоммичен в течение пары дней :)

## wormax-bot - creating model-based RL algorithm for multiplayer video game with restricted frames available due to online nature of the game

The main challenge of this project is playing online video game but given little number of frames compared to existing solutions for Atari benchmark.

## What is already done:
0. Behavioral cloning on 3-4 hours decent human example https://www.youtube.com/watch?v=ccmiViWMPVw&lc=UgySyYfXsdk1yxzoX_J4AaABAg
1. VAE was trained on data collected from 10 hours footage of BC playing the game. Small dimensional latent game representation was acquired.
2. Mixture Density Network was implemented and tested on toy data. [demo](anim.gif)  
**--> You are here <--**  
3. World Model consisting of RNN + MDN was trained on BC gathered data.
4.   
   * Model Predictive Control using World Model with Random Shooting.
   * --//-- with CEM-ES.
   * --//-- with MCTS.
5. Dyna-style model-free algorithm training provided with real evironment data and imagined data from World Model.

## Analogues 
(bad perfomance, model-free approach) http://cs229.stanford.edu/proj2019aut/data/assignment_308832_raw/26588099.pdf  
https://sites.google.com/view/modelbasedrlatari/home

## Sources
1. World models https://worldmodels.github.io/
2. VAE https://lilianweng.github.io/lil-log/2018/08/12/from-autoencoder-to-beta-vae.html#vae-variational-autoencoder
3. Model-based RL on Atari https://sites.google.com/view/modelbasedrlatari/home
4. Dyna https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume4/kaelbling96a-html/node29.html
