## wormax-bot - creating model-based RL algorithm for multiplayer video game with restricted frames available due to online nature of the game

The main challenge of this project is playing online video game but given little number of frames compared to existing solutions for Atari benchmark. And also online format poses challenge of playing versus humans.

## What is already done:
0. Behavior cloning on 3-4 hours decent human example  
1. VAE was trained on data collected from 10 hours footage of BC playing the game. Small dimensional latent game representation was acquired.
2. Mixture Density Network was implemented and tested on toy data.   
3. World Model consisting of RNN + MDN was trained on BC gathered data.  
**--> You are here <--**  
4.   
   * Model Predictive Control using World Model with Random Shooting.
   * --//-- with CEM-ES.
   * --//-- with MCTS.
5. Dyna-style model-free algorithm training provided with real evironment data and imagined data from World Model.

## Step-by-step progress  
0. Behavior cloning on human recording.   
The code for this stage is not present in this repository and can be found [here](https://github.com/LeonidMurashov/Python_Projects/tree/master/Keras/Wormax).  
Result: [video](https://www.youtube.com/watch?v=ccmiViWMPVw&lc=UgySyYfXsdk1yxzoX_J4AaABAg)   
1. Trainging VAE.  
Implementation: [cvae.ipynb](cvae.ipynb)  
Its role here is to embed game frame (128, 128, 3) into latent vector (256), so RNN model can operate more efficiently on compressed representation.  
2. MDN was implemented for toy one dimensional data.  
Implementation: [MDN.ipynb](MDN.ipynb)  
Result: [demo/anim.gif](demo/anim.gif)  
3. MDN was modified to work with high-dimensional data.  
Implementation: [MDN-several-outputs.ipynb](MDN-several-outputs.ipynb)
4. MDN-RNN implemented and tested on toy data (stochastic sines).  
Implementation: [MDN-RNN.ipynb](MDN-RNN.ipynb)
5. MDN-RNN was modified to work with high-dimensional data (two stochastic sines).   
Implementation: [MDN-RNN-ndim.ipynb](MDN-RNN-ndim.ipynb)   
6. BC 4 hours (definitely need more) footage was recorded and fed through VAE  
Implementation: [cvae-latent-extraction.ipynb](cvae-latent-extraction.ipynb)   
Result: [demo/wormax_vae.mp4](demo/wormax_vae.mp4)  
7. World Model (MDN-RNN) was trained of encoded footage  
Implementation: [MDN-RNN-video.ipynb](MDN-RNN-video.ipynb)   
Result: [demo/wormax_mdnrnn_better.mp4](demo/wormax_mdnrnn_better.mp4)  
#TODO: continue  

## Analogues 
(bad perfomance, model-free approach) http://cs229.stanford.edu/proj2019aut/data/assignment_308832_raw/26588099.pdf  
https://sites.google.com/view/modelbasedrlatari/home

## Sources
1. World models https://worldmodels.github.io/
2. VAE https://lilianweng.github.io/lil-log/2018/08/12/from-autoencoder-to-beta-vae.html#vae-variational-autoencoder
3. Model-based RL on Atari https://sites.google.com/view/modelbasedrlatari/home
4. Dyna https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume4/kaelbling96a-html/node29.html
