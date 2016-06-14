:tocdepth: 2

.. sectnum::

.. _change-record:

Change Record
=============

+-------------+------------+----------------------------------+-----------------+
| **Version** | **Date**   | **Description**                  | **Owner**       |
+=============+============+==================================+=================+
| 1.0         | 6/11/2016  | First version.                   | Jacek Becla     |
+-------------+------------+----------------------------------+-----------------+



.. _intro:

Introduction
============

This document describes the project planning processes and tools used in the
DM Subsystem, with particular emphasis on software development.

LSST is now in construction, funded through NSF MREFC. The planning process has
to conform to all government standards and requirements, including mandated
Risk and Earned Value Management System (EVMS).

The team responsible for delivering the LSST DM Software is approaching 100 engineers and
scientists, and is highly distributed geographically. It is essential all processes are robust
and clearly defined, and everyone understands how to apply them; what tools to use and how.

The DM Software is large and complex, and will be written over the entire period of
the construction (7 years). To ensure the team delivers production-quality software
that meets the baseline specification on time and within budget, having a solid, realistic,
resource-loaded, well maintained long-term plan is a must. Further,
appropriate tools and processes need to be in place to track the progress and
execute the long-term plan.

Using modern techniques, in particular the Agile Process, is extremely useful in particular
for short-term planning, managing short-term activities, and maximizing
the team's efficiency.

The project planning processes described in this documents have been structured to
address all of the above (often not fully aligned!) needs. It is a fusion of
the Earned Value Management System, and the Project Planning with Agile Process.


.. _baseline-plan:

DM Project Management Planning Process
======================================

This section explains how the DM Subsystem approaches project planning and plan execution.

Baseline Documents
------------------

The baseline design and architecture of the DM Subsystem is captured through a set of change-controlled
documents, including:

* LDM-148 DM System Design

* LDM-151 DM Applications Design

* LDM-152 DM Middleware Design

* LDM-135 DM Database Design

* LDM-131 DM SUIT Conceptual Design

The complete set of DM baseline documents can be found in Docushare, Collection-2511.

All together, this collection of documents capture all work DM has to deliver during the LSST Construction.

Planning Packages
-----------------
The work is divided into *o(few hundred)* concrete, technical *packages of planned work*. The packages divide work
at the 3rd Level of WBS, e.g., typically a 3rd Level WBS is broken down into 20-50 packages. Each such package
addresses a piece of work defined in the baseline, and all together they cover the entire DM Baseline.
Each package has a clearly defined scope, deliverable(s), resource cost, and an end date. Additionally,
each package keeps track of which section(s) of which baseline document it implements.



In the EVMS world, these packages are implemented directly as *Planning Packages* (PP).

Milestones
----------
All significant development stages of each planning package are tracked through *milestones*.
Each planning package has at least one milestone, used to mark the completion of a given package.
It is not uncommon to have multiple milestones per package to track progress along the way.
Milestones can be related to multiple planning packages, potentially from different WBSes.
Each milestone has a description, and due date; it has no duration, and no resources assigned to it.
It is not uncommon for a milestone to related to multiple planning packages, possibly from
different WBSes.

Each activity within a planning package that involves a cross-team dependency is required to end with
a milestone; this includes activities related to delivering software components, hardware, and services.

Further, milestones have *levels*:

* Level 1 denotes the most important milestones exposed at the NSF level

* Level 2 denotes cross-subsystem milestones (for example, DM milestones that affect the Camera Subsystem)

* Level 3 denotes cross-team milestones within a subsystem (for example, Middleware milestones that effect the DRP Team)

* Level 4 denotes internal milestones within a team.

*O(few hundred)* milestones have been defined to-date to track the progress of DM activities.

Relationship between milestones, as well as between milestones and planning packages are captured:
milestones typically *block* planning packages, milestones can also *relate* to other milestones.

Baseline Long-Term Plan
-----------------------

Planning packages, together with milestones form the *Baseline Plan*. The plan is under change control.

The plan is stable. Any change to the plan, including changing scope, cost or schedule, must be approved
by the appropriate change control body:

* Change Control Board approval for any non-trivial change to a planning package or Level 1 and
  Level 2 milestone

* DM's TCT approval for Level 3 milestones

* no approval is needed for Level 4 milestones, however any non-trivial change must be communicated
  to the DM team

* trivial changes, such as small corrections / clarifications to narrative that do not affect
  scope, time or budget are allowed without approval.

Typically, adjustments to Level 1, 2 and 3 milestones are made every 6 or 12 months. Changes to Level 4
milestones can occur more frequently.

Short-Term Planning
-------------------

The short-term plan is managed through *epics* and *stories*, and executed through *cycles*.

In the EVMS world, epics map directly to *activities*, and stories map to *activity steps*.

Epics and Stories
~~~~~~~~~~~~~~~~~

Typically, planning packages encompass relatively large blocks of work. To plan and execute work
in details, finer-grain planning is required. This is implemented through epics and stories.

Each epic captures a non-trivial work that is associated with a subset of work defined in a
planning package. Each epic has a clear description, well defined deliverables, and
relationships with a planning package (an epic *implements* a PP), and a milestone (an epic
*blocks* a milestone). Epics are resource loaded, and have start and end dates defined.

Each epic is broken into smaller chunks of work, called *stories*. Stories are primarily used
to define and manage the short-term activities of individual developers.

Epics and stories are used to track all software work, as well as work on delivering hardware and
services that are tightly coupled with software (example: "Deliver OpenStack-based Test Cluster
running RedHat 6.1".) Details of work on standalone activities do not have to be captured on daily
bases through stories (example: "Deliver 10Gbit link between Chile and USA")

.. _cycles-and-releases:

Cycles and Releases
~~~~~~~~~~~~~~~~~~~

The work is executed through 6-month *cycles*. The scope of work for each cycle is driven by the
Baseline Plan, in particular by milestones. Each cycle ends with a new software release. Releases are
thoroughly tested and documented.

Cycles are planned through *epics*. Each epic must be defined such that it can be completed
within a single cycle.

Once a plan is defined for a given cycle, it is loaded into PMCS and changed-controlled. A plan for
a cycle is loaded to PMCS during the month proceeding the start of the cycle.

Any non-trivial adjustments to the plan that affect scope, schedule or budget must be approved
by CCB.

It is acceptable to load the plan in 3-month chunks, e.g., the plan for
the first 3 months of the cycle is loaded before the start of the cycle, and the remaining
part of the plan covering the last 3 months is loaded before the 4th month starts. This
allows for minor fine-tuning of the second half of the cycle without going through the CCB
approval.

Level of Effort
---------------

Two general rules are applied for the DM Team labor when determining whether an activity should be
treated as LOE or non-LOE:

* All activities that have a clear deliverable are tracked through non-LOE. Examples of non-LOE
  activities include writing a new piece of software, purchasing new equipment, or adding new
  machines to the cluster.

* Activities that can not be predicted, as well as short, recurring routine activities are considered LOE.
  Examples of LOE activities include replacing faulty disk drive, cluster maintenance, or writing monthly
  status report.

For planning purposes, 70% of available time of each software developer is assumed to be available
for "pure, uninterrupted coding", and the remaining 30% is considered as "overhead", and tracked
explicitly as LOE.

A small fraction of all DM labor is performed by contractors. The contractor labor is managed as LOE,
directly in dollars.

People
======

* DM Project Manager responsible for overall plan, schedule and priorities.

* Work divided into smaller pieces, through WBS.

* Each piece has a dedicated technical manager.

* Main responsibilities of technical managers:

  * Assemble the team capable of delivering work scoped through the WBS on-time and within budget.
    Provide daily technical management and leadership for the team, monitor and optimize team performance.

  * Work closely with the DM Project Manager on defining short and long-term plan and schedule for
    their teams. Direct the execution of their team's plan, ensuring the team delivers on-time and within budget.

  * Report group's activities as required, including reporting to the Earned Value Management System (EVMS)
    used by LSST, and providing input for monthly status reports.

* In a sense, DM PM "owns" the overall baseline plan (PPs, milestones), and technical manager "own" epics.


Tools
=====

The master copy of the Baseline Plan, which includes all planning packages and all milestones is captured
in Primavera. This is always the authoritative source of truth for the Baseline Plan.

Information about milestones is also kept in JIRA DM Baseline Plan (DMBP) project, and is periodically
synchronized with Primavera. Having milestones in JIRA is, in particular, useful for expressing blocking
relationships between milestones and epics between different teams.

The master set of epics and stories is kept in JIRA "DM" project. Epics corresponding to the current
and upcoming cycles are snapshotted and loaded to Primavera.

Information in JIRA for the current cycle is particularly important: it needs to be
kept up-to-date and it should reflect the current state of development. Progress
updates for activities that block other teams, in particular when the delivery date
approaches, are expected to be provided promptly (depending on urgency, weekly or even daily)


The JIRA DMBP serves as an easy-to-use interface that TCAMs can use to interact with
the Baseline Plan. Changes made to the JIRA DLP are periodically submitted to CCB
and transferred to the Primavera when approved (every 6 or 12 month). The Primavera
version is always the authoritative source of truth.

.. image:: baselinePlanDiagram.png


The above diagram summarizes what needs to be approved by CCB, what is stored in
Primavera, and what is stored in JIRA.
