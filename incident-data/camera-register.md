# Camera Register — Building A

Six cameras, continuous recording, 30-day retention, no offsite backup.

| Camera | Status | Location | Recorded coverage |
|---|---|---|---|
| CAM-1 | Online | Main office exterior | Office entrance, street side |
| CAM-2 | Online | Main office interior | Front desk, waiting area |
| CAM-3 | Online | North hallway | North corridor, rooms 1–11 |
| CAM-4 | Online | West entrance | Vehicle gate, west walkway |
| CAM-5 | Online | Library interior | Stacks, reading tables |
| CAM-6 | **OFFLINE since 2026-06-11** | South pedestrian gate | — |

## Coverage map (as built)

```
                    NORTH BUILDING
   ROOM 1  ROOM 2  ROOM 3  ROOM 4  ROOM 5  ROOM 6
     |       |       |       |       |       |
     +-------+-------+-------+-------+-------+
     |            [CAM-3]                    |
     |        NORTH HALLWAY                 |
     +----------------+---------------------+
                      |
   [CAM-2]            |              [CAM-5]
   MAIN OFFICE        |              LIBRARY
        |             |                   |
  ------|-------------|-------------------|------ SOUTH
        |             |                   |
    [CAM-1]       (stairwell)          CAM-6 OFFLINE
   exterior         NO CAMERA          south ped gate
                    NO CAMERA
```

## Uncovered locations

There is **no camera** covering:

- The **south stairwell** (CAM-3 stops at the north hallway)
- The **basement plant room**
- The **staff parking area**
- The **archive room** inside the library (CAM-5 covers the reading area only)
- The **server closet corridor**

## Footage requested vs. available

Facilities pulled the following footage in response to the incident report:

| Requested | Available | Notes |
|---|---|---|
| CAM-1, 2026-09-28 20:00 – 2026-09-29 07:00 | **Yes** | Continuous |
| CAM-2, same window | **Yes** | Continuous |
| CAM-3, same window | **Yes** | Continuous |
| CAM-4, same window | Yes, but **grainy and low-contrast after 22:00** | Parking lot unlit; IR illuminator appears to have failed |
| CAM-5, same window | **Yes** | Continuous |
| CAM-6, same window | **NO — camera offline** | Requested 2026-09-30, still offline |

## Maintenance

A work order to replace the CAM-4 infrared illuminator was raised
2026-06-14. It is still open. A work order to repair CAM-6 was never raised.
