:tocdepth: 2

.. sectnum::

.. _change-record:

Change Record
=============

+-------------+------------+----------------------------------+-----------------+
| **Version** | **Date**   | **Description**                  | **Owner**       |
+=============+============+==================================+=================+
| 0.1         | 3/06/2016  | Initial version.                 | Jacek Becla     |
+-------------+------------+----------------------------------+-----------------+

.. warning::

  This is a very early and incomplete draft (more like a collection of thoughts and notes) to stimulate discussion. In particular, note that information does not flow as it should, for example, we are talking about jira, story points etc before they are properly introduced. This will all need to be fixed.


.. _intro:

Introduction
============

* LSST construction = large team, long term, complex software

* need robust project management process

* funded under NSF MREFC, process needs to be formal

* need realistic plan. Resource-loaded, covering entire construction

* need to maintain the plan, to track progress and fully execute the plan

.. _baseline-plan:

Baseline DM Plan
================

The baseline design and architecture of the DM subsystem is captured through a set of change-controlled documents:

* (list them here, DPDD, apps, middleware, DB, cost model etc)

These documents describes all work that needs to be done.

Work is divided into smaller activities, called *epics*. All epics are resource-loaded. Execution of the work is tracked through *milestones* which mark specific deliverables along the project timeline.

Every non-trivial activity requiring few FTE-month work is explicitly captured. This leads to o(few hundred) milestones and o(thousand) epics.

Each milestone has a **description**, and **due date**. It has no duration, and no resources assigned to it.

Each epic has: a clear **scope and deliverable(s)**, **resource cost**, and an **end date**. It also tracks which section of which baseline document it addresses (this needs to be implemented). This simplifies verification whether all parts of the baseline have been captured in the plan.

There is a well defined relationship between epics and milestones: epics block milestones, milestones can block other milestones.

The baseline plan (milestones and epics) is under change control. Every non-trivial adjustment to scope, cost or schedule requires approval of the CCB.


The baseline plan has been assembled using a mix of top-down and bottom-up analysis. Top-down analysis involved analyzing project-level requirements and risks, as well as the DM requirements and baseline architecture for all components of the DM subsystem. Bottom-up analysis involved analysing all activities that need to be done and estimating their cost through prototyping and research as needed. [footnote: major replanning undertaken 1 1/2 year after start of construction]

Updating Baseline
=================

Small adjustments to the baseline can be made by TCAMs in agile way. This includes small changes to SPs, moving SPs between activities, changing dates etc. All such changes are tracked and revisited semi-annually. Impact on scope, cost and schedule is revisited and if it is above pre-set level, the changes are submitted to CCB.

Major changes that have potential to significantly impact scope, cost of schedule need to be discussed at DMLT and approved by TCT before they can be implemented.

This gives TCAMs agility and flexibility to adjust their plans, while we ensure the scope/cost/schedule is well controlled and managed.




.. _cycles-and-releases:

Cycles and Releases
===================

* All work captured in the Baseline Plan is divided into 6-month "cycles"

* Scope of each cycle is driven by the Baseline Plan, in particular by milestones.

* Each cycle ends with a new software release

  - releases are thorougly tested. They come with documentation


People
======

* DM Project Manager responsible for overall plan, schedule and priorities.

* Work divided into smaller pieces, through WBS.

* Each piece has a dedicated technical manager.

* Main responsibilites of techical managers:

  * Assemble the team capable of delivering work scoped through the WBS on-time and within budget. Provide daily technical management and leadership for the team, monitor and optimize team performance.

  * Work closely with the DM Project Manager on defining short and long-term plan and schedule for their teams. Direct the execution of their teams's plan, ensuring the team delivers on-time and within budget.

  * Report group's activities as required, including reporting to the Earned Value Management System (EVMS) used by LSST, and providing input for monthly status reports.


.. _planning:

Planning
========


.. _cycle-planning:

Cycle Planning
--------------

* plan all 6 months

  - detailed plan for all non-LOE work, resource loaded

  - (describe spreadsheet here)

* load the first three months

* fine-tune the last three months, load in 2nd month + LCR

* building realistic plan

  - not adding any *artificial* padding or buffers

  - reserving time for expected problems/bugs/issues

  - each piece of work clearly defined, scoped, with clear deliverables, not just "continue doing x"

    + research activities time-boxed

  - Reserving time to do exploration and research necessary to well understand scope / resource-load work planned for cycle x+1.

  - Reserving time for cross-team discussions (recommended ~2-3 days per each team pair)

  - Reserving time for documentation, recommended 1-2 week sprint at the beginning of cycle to
    bring all documentation up to date with the work done in previous cycle

* while doing cycle plan, combing through the backlog (the list of all work), reordering as needed

* plan is verified and issues such "overloaded developers" are caught



Resource loading a cycle
------------------------

* 1800 h/year

* 150 per month

* adjusting to capture LOE time, eg, tcam spending 50% on non-coding

* adjusting to capture science time (20%)

* applying 30% overhead for ...

* left: xx h, = 26.3 story points per FTE-month

* 1 FTE-month = 26.3 SPs

* the size of the team determines the pool of available story points

* assigning available story points per developer



Resource loading for bugs
-------------------------

.. warning::

  this needs thinking

There are two schools:

* bugs should have story points. This helps to understand real velocity

* bugs should not have stories points because developers already earned value for completing the story that led to the bug, and they should not receive more points for it, they shouldn't have earned the points to begin with

(need to decide, Camera Team does the later. I am leaning towards the former, reserving reasonable number of story points in the long term plan for bug fixes, carefully tracking story points used for bug fixes in each cycle, and adjusting the planned number of story points for bug fixes in future cycles based on findings)

Related reading:

* http://programmers.stackexchange.com/questions/162145/story-points-for-bug-fixing-tasks-is-it-suitable-for-scrum

* http://www.infoq.com/news/2011/01/story-points-to-bugs


Sprints and Boards
------------------

* monthly cadence

* defining stories

  - assign to developers

    + each story should have >0 SPs

  - related docs: https://confluence.lsstcorp.org/pages/viewpage.action?pageId=21397653

* each team should have a board (scrum for non-LOE, kanban for LOE).

* this includes kanban DMLT board, kanban DM Sys Eng board

* for LOE: no need to capture repeated, obvious LOE tasks, but if there is any work that is worth telling others about, capture it through a story on kanban board

* monthly sprints

* 5 min/team sprint report during DM-AHM virtual standup at the beginning of each month

* DM-AHM short presentations from each team at the beginning of each cycle introducing work planned for upcoming cycle

* central DM board

* schedule appropriate number of SPs each sprint, don't let it fall behind

* avoid adding stories to sprint except blockers / crititical.

* looking at burndown charts every month


Keeping Plan Up-to-date
-----------------------

As the need to adjust the plan arises, we:

* estimate scope and/or cost change

* if the impact is small/moderate, we model it in the plan: add new epic(s) and/or milestone(s), re-schedule to make sure plan is not overloaded. Accumulated changes are submitted to CCB for approval semi-annually. Once approved, updated baseline is released.

* if the impact is large CCB approval is seeked immediately




Tools
=====

* Master copy of all DM milestones in PMCS

* Master copy of of all epics covering software-related work in JIRA DM project

* For milestone-based drill down we use spreadsheet
  - generated monthly from PMCS, available online in shared space
  - enables drill down per milestone level, per WBS, per FY, what blocks what
  - this will replace LDM-240

* For epic-based drill down we use live, webbased tool
  - like http://slac.stanford.edu/~becla/tmp/ldm-240.html
  - drill down per WBS, per FY

* JIRA DLP - default interface for TCAMs to enter info about milestones
  and blocking relationships
  - TCAMs do not have to use DLP: to update milestones, tcams use DLP, or tell Kevin
  - Kevin will have tool to synchronize PMCS / JIRA DLP (both ways)
  - we are getting rid of meta-epics

* JIRA DM project

  - tracks all non-LOE software work

    + the master copy of all software activities in JIRA

    + for hardware and network related activities, when convenient, master plan can be in PMCS, monthly exports to JIRA DLP. It is in particular important to export to DLP the milestones that block software development.

  - tracks all random tasks (eg tcams todo)

* JIRA DLP project

  - tracking milestones and resources for all work that relates to software (eg. related to software directly, or impacts/blocks software dev activities)

  - DM epics block DLP milestones

  - semi-stable, semi-agile, bridges the two worlds

* PMCS

  - tracking milestones, budget, resources for ALL work, including software, networks, hardware

  - stable, rigid plan

  - refer to LPM-98 for further details

* custom tools on top of JIRA and PMCS

  - eCAM, refer to LPM-98

  - We can see all the epics, per WCS, per FY, we can resource load it etc, like I did here
    http://slac.stanford.edu/~becla/tmp/ldm-240.html

  - Improve DLP, make it useful to drill down on from milestone-perspective

  - maybe build graphical interface on top showing milestone dependencies (rely on is-blocked-by links from jira)

    + with live links to baseline docs

    + with live links to epics

    + drill down per wbs, per milestone level, per FY

  - scripts for monitoring / flagging / alerting

    + mark epics in progress when stories in progress/done

    + sum of story points for all stories in epic significantly differs for epic SP estimate

    + stories in progress for too long

    + stories too large

    + - too many stories per developer in a month

    + etc


JIRA
----

* tracks every piece of work, every task, every non-trivial activity that needs to be done during construction

* organized into epics and stories

* effort is tracked through story points

* epics are blocking milestones

* to complete a milestone, all blocking epics must be completed

* every major piece of work captured as an epic

* every epic is assigned to WBS

* epics are assigned to FYs.

* every epic has story points

  - SP = 4 hours of uninterrupted work

* epics linked to sections of baseline documents

* activities that do not (yet) fall into any obvious epic, simply create a story, it will end up on the backlog

  - if there are several free-floating stories that are related, create an epic for them. If it is not assigned to any FY, it will be assumed it is done after the last epic assigned with FY is done.

* every epic and every story must have "Team" set, this ensures there is a TCAM responsible

* using dueDate if it is needed by specific date

* exposing all relationships, especially dependencies that might block you. If there is no place to show dependency on, work with corresponding tcam and make sure it gets created

* only assign a person to a story when it is known for sure that given person will be the one working on that story. In practice, names should be assigned to stories when planning resources for current/next cycle, or when something urgent/critical comes up, or when it is really trivial (< 0.5 SP). Otherwise leave as "Unassigned", unless there is only one and only expert that can handle a given story.



JIRA Best Practices
~~~~~~~~~~~~~~~~~~~

* no stories with more than ~26 SPs! (we have a few that are above 100)

* stories should not span sprints

* each done story should have clear deliverable

  - see DM-3761

* don't overload people, 50+ SPs for a single person in a month is not realistic


JIRA and current cycle plan in PMCS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* All epics that are part of current cycle are considered "PMCS-locked".
  That means changes to scope (eg, description) and resources (eg story points)
  can only be made by the TCAM responsible for given epic (typically with
  consultation with Kevin)

  - note that having cycle field set does not make it PMCS-locked. It must be
    set to current cycle

* TCAMs should monitor all changes to activities assigned to their team
  (rss feed is good for that)

PMCS
----

(short descr what it gives us)


Custom Tools
------------

(mention eCAM)

mention spreadsheet
 - can drill down ...

Reporting Process
=================

Reuse http://developer.lsst.io/en/latest/processes/project_planning.html#data-management-reporting-process

Introduce:

* monthly cycle reports, 5 min/team, all hands, virtual, plus short discussion

* cycle introduction meeting 15 min per team, right when cycle starts, ahm, virtual
