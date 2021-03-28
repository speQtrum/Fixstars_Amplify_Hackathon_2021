# Fixstars Amplify Hackathon 2021
Application submission repository for Fixstars Amplify Hackathon 2021
### Even Odd Classification using Combinatorial Optimisation Approach
![alt text](https://code4coding.com/wp-content/uploads/2019/03/evenoddarray.jpg) <br>

Here I have presented a combinatorial optimisation approach for even-odd number classification from an array of integers. Implementation with Fixstars Amplify and Fixstars D-wave has been shown. At the conclusion the accuracy and performance analysis is given with vanilla D-wave implementation. <br>
For detail please visit jupyter notebook file. <br>

![alt text](https://github.com/speQtrum/Fixstars_Amplify_Hackathon_2021/blob/main/result.png) <br>

```shell
$ python submission.py
```

### **Conclusion**
This approach provides a new way of separating even-odd numbers from an array using combinatorial optimisation method and provides promising result like classical. <br>
**When the size of the input array becomes larger, Amplify clients (also amplify d-wave wrapper) starts to mis-classify the integers, where vanilla D-wave (QPU and hybrid) gives perfect (100% aaccurate) results even with very large inputs.** This might work as a feedback, and can help to improve fixstars experiences. <br>
Vanilla D-wave implementation link with 500 integer inputs: https://colab.research.google.com/drive/1LJba0qFKqg8-8lFHlvn-9AZ1gb4MUBhg?usp=sharing

<br>
Reproduction of results for scientific paper publication is strictly prohibited without permission. <br>
©2021 Aniruddha Biswas. All rights reserved.
