
      const climbStairsR = (stepCount) => {
        if (stepCount === 1) {
          return 1;
        } else if (stepCount === 2) {
          return 2;
        } else {
          return climbStairsR(stepCount - 1) + climbStairsR(stepCount - 2);
        }
      };

      const climbStairsI = (stepCount) => {
        let steps = [];

        // Base Cases.
        steps.push(0);
        steps.push(1);
        steps.push(2);
        for(let i = 3 ; i <= stepCount ; i++) {
          steps.push(steps[i - 1] + steps[i - 2]);
        }
        return steps[stepCount];
      };

      const climbStairsNM = (stepCount, limit) => {
        let steps = [];
        steps.push(0);
        steps.push(1);
        for(let i = 2; i <= stepCount ; i++) {
          console.log(`I: ${i}`);
          steps.push(0);
          console.log(`Array steps: ${steps}`);
          const len = steps.length - 1;
          console.log(`Len: ${len}`);
          for(let j = 1; (i - j) > 0; j++) {
            console.log(`J: ${j}`);
            console.log(`when j: ${j}, steps[len]: ${steps[len]}, steps[len - 1]: ${steps[len - 1]}`);
            steps[len] = steps[i - j] + 1;
            console.log(`steps[len]: ${steps[len]}`);
            console.log(`Steps: ${steps[len]}`);
          }
        }
        console.log(steps[stepCount]);
      };


      const steps = Number(prompt("Enter Step count: "));
      climbStairsNM(steps, steps);
      // console.log(`Step Count Iteration: ${climbStairsI(steps)}`);
      // console.log(`Step Count Recursion: ${climbStairsR(steps)}`);
