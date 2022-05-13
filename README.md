
# Drivable Ground Path Detection Using Semantic Segmentation

Project - 04 for the course, 'ENPM673 - Perception for Autonomous Robots' at the University of Maryland, College Park.

Implementation of detecting the drivable path in the ground plane for a mobile robot in an indoor environment using Semantic Segmentation (U-Net) on a custom collected dataset on the campus of the University of Maryland, College Park.


## Team Members:
* Adarsh Malapaka (118119625)
* Kumara Ritvik Oruganti (117368963)
* Sai Sandeep Adapa (118411460)
* Sparsh Bhogavilli (117552515)
* Venkata Sai Ram Polina (118436579)

<!-- ## Required Libraries: 
* cv2 : To add arrows, lines or circles in the map at the desired coordinates.
* time: To calculate the running time for the A* algorithm.
* numpy: To define the obstacle map matrix
* argparse: To parse command line arguments
* random: To generate random nodes
* copy: To create copy of lists -->

<!-- ## Dataset: -->
  

<!-- Obstacle Map (Known)    |  Modified RRT* Tree Expansion | Modified RRT* Path
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/40534801/167329665-c65a21f8-3b64-4925-8e94-7a847503f285.png" width="100%"> | <img src="https://user-images.githubusercontent.com/40534801/167330587-facbd5db-6b99-4972-b291-59e6340eb1c3.png" width="100%"> | <img src="https://user-images.githubusercontent.com/40534801/167330631-e732874c-8a28-4649-8a1b-71ff50090f0c.png" width="100%">

Optimized Modified RRT* Path   |  Obstacle Map - Known (Blue) & Unknown (Green) | Optimized Re-planned Path
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/40534801/167331983-65292dcd-b260-40a0-8279-db557a60bf40.png" width="100%"> | <img src="https://user-images.githubusercontent.com/40534801/167332002-ada4a3d2-35bf-4e24-bc73-29de6ac63951.png" width="100%"> | <img src="https://user-images.githubusercontent.com/40534801/167332042-98f6c1f4-d4c0-490d-a6f5-b5aa75e53d2e.png" width="100%">


## For Map 02:
  [co-ordinates with respect to bottom left corner origin of the window]
  
	Start-Node: (10, 10)

	Goal-Node:  (350, 150)
	
	Robot Clearance: 5

Obstacle Map (Known)    |  Modified RRT* Tree Expansion | Modified RRT* Path
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/40534801/167329737-44ea40fd-6255-4a18-9f05-a2e38ca3b333.png" width="100%"> | <img src="https://user-images.githubusercontent.com/40534801/167331089-978f5144-44b3-477f-b77b-fd82c650bfba.png" width="100%"> | <img src="https://user-images.githubusercontent.com/40534801/167331109-de378cf9-1e99-447b-a2e0-cd81c54cd3b5.png" width="100%">

Optimized Modified RRT* Path   |  Obstacle Map - Known (Blue) & Unknown (Green) | Optimized Re-planned Path
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/40534801/167332117-9a107ef2-3c50-446f-8900-190e4f0c8003.png" width="100%"> | <img src="https://user-images.githubusercontent.com/40534801/167332146-adc8588a-e6a3-4d52-a649-8c60c37872fd.png" width="100%"> | <img src="https://user-images.githubusercontent.com/40534801/167332180-f4419940-7bcf-42de-a14d-5c9901b8b91b.png" width="100%">


#### Note: 
The shapes in the map including the outer boudary walls have been bloated by robot clearance amount on all sides.
  
## Running the Code:

The code map number as an argument.

**Format/Syntax:**

		  'python3 mod_rrt_star.py <map-argument>'
      
**For Map 01:**	
  
		  'python3 mod_rrt_star.py --map1'
      
**For Map 02:**	

		  'python3 mod_rrt_star.py --map2'
      
#### Note: 
The algorithm is dependent on the randomly generated nodes.  If the nodes are not sufficient (i.e. the path converges very quickly), the algorithm maynot find a feasible path avoiding the obstacles. Hence, it is adviced to rerun the program again.
If the path doesn't converge, rerun the program using the above commands after pressing the ctrl+c to force quit the current run. -->
