VAMPyR coven
=====================

This is a collection of notebooks for VAMPyR, the Very Accurate Multiresolution Python Routines library. The repository holds Jupyter notebooks that demonstrate the use of VAMPyR for various scientific computations and simulations.

The setup notebook provides instructions for installing and configuring the VAMPyR library and its dependencies, ensuring the environment is prepared for all subsequent simulations.

.. toctree::
   :hidden:
   :maxdepth: 1

   setup

The demos include:

- The beryllium atom notebook, where users can learn about quantum mechanical modeling of the beryllium atom, including setting up the atomic structure, calculating energy levels, and visualizing electron orbitals using VAMPyR.
- The harmonic oscillator evolution notebook guides users through the simulation of the time evolution of a quantum harmonic oscillator, demonstrating the use of VAMPyR to solve the Schrödinger equation and analyze system dynamics.
- The PCMSolvent notebook focuses on the application of the Polarizable Continuum Model (PCM) for simulating solvent effects. It shows how VAMPyR can be used to model the influence of a solvent as a polarizable continuum on a solute molecule.

These notebooks can be run directly in the browser for convenience, but for those who prefer or require local execution, it is also possible to download the repository and run the notebooks on one's own machine.

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Demos

   notebooks/beryllium_atom
   notebooks/harmonic_oscillator_evolution
   notebooks/PCMSolvent
