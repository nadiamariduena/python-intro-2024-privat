## 🤦 slow after UBUNTU upgrade

<br>

---

<br>

### CREATE more virtual MEMORY

https://www.baeldung.com/linux/proc-meminfo

```js
//1   Check the amount of swap you have
grep SwapTotal /proc/meminfo
//
// 2 Turn off the swap process
sudo swapoff -a
//
// 3 Resize the swap (in my case I expanded it to 16 GB)
sudo dd if=/dev/zero of=/swapfile bs=1G count=16
/*

👍 result
before adding that command 3, i had this:
SwapTotal:       2097148 kB
which corresponds to 2GB

after i typed that command
SwapTotal:             0 kB
// but at the end we will pass from having 2GB to the memmory, to 16GB
*/
//
// 4 Attach the swap to the partition
sudo mkswap /swapfile
//
// 5 Activate swap (enable it)
sudo swapon /swapfile
//
// 6 See the new swap size
grep SwapTotal /proc/meminfo
```

<br>

### result

- The command you provided effectively removed the existing swap space (which was approximately 2 GB in your case) and replaced it with a new swap file of 16 GB, as specified.

#### Whether this change is "good" depends on the specific requirements and usage patterns of your system:

Increased Swap Space: The new swap file of 16 GB provides more virtual memory compared to the previous 2 GB. This can be beneficial if your system frequently runs out of physical RAM and needs to rely on swap space to prevent crashes or performance degradation.

Potential Impact on Performance: However, increasing swap space isn't always beneficial. Excessive swapping, where the system frequently moves data between physical RAM and swap space, can lead to decreased performance due to the slower access times of disk storage compared to RAM.

Disk Space Usage: Additionally, the new swap file consumes disk space. If disk space is limited and the system rarely uses swap space, creating a large swap file may not be optimal.

Customization and Optimization: Swap space size should ideally be tailored to the specific needs of your system. It's not a one-size-fits-all solution. Consider factors such as the amount of physical RAM, the types of applications you run, and the typical workload of the system.

In summary, whether the change is good or not depends on your system's requirements and usage patterns. If you frequently encounter memory-related issues and the system benefits from additional swap space, the change might be beneficial. However, if the system rarely uses swap space or if disk space is limited, you might need to reconsider the swap file size or explore alternative solutions.

<br>
<br>

## 🌈 So its like the part of our brain humans dont use?

<br>

#### In a sense, you can think of swap space in computing as similar to the unused parts of the brain. 🍭

Just as the brain has certain areas that aren't actively engaged in cognitive tasks all the time, a computer system may have portions of its physical RAM that aren't currently being utilized. When the physical RAM becomes full, the operating system can use swap space (like the swap file created by the command) to temporarily store less frequently accessed data or processes, similar to how the brain might shift less critical functions to less active areas.

So, in this analogy:

Physical RAM represents the active, engaged parts of the brain, where immediate processing and storage occur.
Swap space represents the less active or unused parts of the brain, where less critical or less frequently accessed data can be temporarily stored when the active parts are full.
Both swap space and the "unused" parts of the brain serve to expand the capacity or capabilities of the system without needing immediate access to all resources simultaneously. However, it's important to note that while swap space can help prevent memory-related issues like crashes due to insufficient RAM, excessive swapping (similar to excessive use of unused brain areas) can lead to performance degradation in a computer system.

<br>

<br>

# so is this good?

```java
SwapTotal: 2097148 kB

after i typed that command
SwapTotal: 0 kB
```

<br>

#### The command you provided effectively removed the existing swap space (which was approximately 2 GB in your case) and replaced it with a new swap file of 16 GB, as specified.

Whether this change is "good" depends on the specific requirements and usage patterns of your system:

🏩Increased Swap Space: The new swap file of 16 GB provides more virtual memory compared to the previous 2 GB. This can be beneficial if your system frequently runs out of physical RAM and needs to rely on swap space to prevent crashes or performance degradation.

Potential Impact on Performance: However, increasing swap space isn't always beneficial. Excessive swapping, where the system frequently moves data between physical RAM and swap space, can lead to decreased performance due to the slower access times of disk storage compared to RAM.

Disk Space Usage: Additionally, the new swap file consumes disk space. If disk space is limited and the system rarely uses swap space, creating a large swap file may not be optimal.

Customization and Optimization: Swap space size should ideally be tailored to the specific needs of your system. It's not a one-size-fits-all solution. Consider factors such as the amount of physical RAM, the types of applications you run, and the typical workload of the system.

In summary, whether the change is good or not depends on your system's requirements and usage patterns. If you frequently encounter memory-related issues and the system benefits from additional swap space, the change might be beneficial. However, if the system rarely uses swap space or if disk space is limited, you might need to reconsider the swap file size or explore alternative solutions.
