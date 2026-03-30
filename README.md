# VChaCha (Variable ChaCha) Stream Cipher
VChaCha is a stream cipher modeled off the ChaCha20 cipher. Rather than operating twenty times to
generate the keystream, VChaCha gives developers the freedom to choose how many operations.
This allows developers to save computation time and power by trading off security.
One use case for VChaCha is for encrypting long, but not very sensitive, blocks of information.

In this repository, we also include a small test function to visualize the computation time as a function of key size,
number of rounds, and plaintext lengths.

## Instructions:
To run this program, navigate to the directory in the terminal and type `python3 vchacha.py` to run the initial tests.
To view the visualizations and time recordings for different inputs, type `python3 benchmarking.py`

## Authors:
Brett Gerlach, Joey Hemmerle, Doanh Phung, Charles Anton Sibal, 
Bryan Wheeler

Forked from [pts/chacha20](https://github.com/pts/chacha20/blob/master)

## AI Disclaimer:
LLMs were used during the brainstorm and test phases of this project.
We utilized LLMs to give us examples of stream and block ciphers, as well as for debugging our test script

More info about ChaCha20:

* https://en.wikipedia.org/wiki/Salsa20
* http://cr.yp.to/chacha.html