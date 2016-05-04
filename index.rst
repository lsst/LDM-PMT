:tocdepth: 2

.. sectnum::

.. _change-record:

Change Record
=============

+-------------+------------+----------------------------------+-----------------+
| **Version** | **Date**   | **Description**                  | **Owner**       |
+=============+============+==================================+=================+
| 0.1         | 4/28/2016  | Initial version.                 | Jacek Becla     |
+-------------+------------+----------------------------------+-----------------+



.. _intro:

Introduction
============

This document describes the project planning processes and tools used in the DM,
with particular emphasis on software development.

LSST is now in construction, funded through NSF MREFC. The planning process has
to conform to all government standards and requirements, including mandated
Risk and Earned Value Management System (EVMS).

The team responsible for delivering the LSST DM Software is approaching 100 engineers and
scientists, and is highly distributed geographically. It is essential all processes are robust
and clearly defined, and everyone understands how to apply them; what tools to use and how.

The DM Software is large and complex, and will be writen over the entire period of
the construction (7 years). To ensure the team delivers production-quality software
that meets baseline specification on time and within budget, having a solid, realistic,
resource-loaded, well maintained long-term plan is a must. Further,
appropriete tools and processes need to be in place to track the progress and
execute the long-term plan.

Using modern techniques, in particular the Agile Process is extremely useful in particular
for short-term planning, managing short-term activities, and maximizing
team's efficiency.

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

* LDM-131 DM SUI Conceptual Design

The complete set of DM baseline documents can be found in Docushare, Collection-2511.

All together, this collection of documents capture all work DM has to deliver during the LSST Construction.

Planning Packages
-----------------
The work is divided into *o(100)* concrete, technical *packages of planned work*. The packages divide work
at the 3rd Level of WBS, e.g., typically a 3rd Level WBS is broken down into 10-20 packages. Each such package
addresses a piece of work defined in the baseline, and all together they cover the entire DM Baseline.
Each package has a clearly defined scope, deliverable(s), resource cost, and an end date. Additionally,
each package keeps track of which section(s) of which baseline document it implements.



In the EVMS world, these packages are implemented directly as *Planning Packages* (PP).

Milestones
----------
All significant development stages of each Planning Package are tracked through *milestones*.
Each Planning Package has at least one milestone, used to mark the completion of a given Package.
It is not uncommon to have multiple milestones per Package to track progress along the way.
Each milestone has a description, and due date; it has no duration, and no resources assigned to it.

Each activity within a Planning Package that involves a cross-team dependency is required to end with
a milestone; this includes actvities related to delivering software components, hardware, and services.

Further, milestones have *levels*:

* Level 1 denotes the most important milestones exposed at the NSF level

* Level 2 denotes cross-subsystem milestones (for example, DM milestone that affect the Camera Subsystem)

* Level 3 denotes cross-team milestones within a subsystem (for example, Middleware milestone that effect the DRP Team)

* Level 4 denotes internal milestones within a team.

*O(few hundred)* milestones have been defined to-date to track the progress of DM activities.

Relationship between milestones, as well as between milestones and planning packages are captured:
milestones typically *block* planning packages, milestones can also *relate* to other milestones.

Baseline Long-term Plan
-----------------------

Planning Packages, together with Milestones form the *Baseline Plan*. The plan is under change control.

The plan is stable, any change to the plan, including changing scope, cost or schedule must be approved
by the appropriete change control body:

* Change Control Board approval for any non-trivial change to Planning Package or Level 1 and
  Level 2 milestones

* DM's TCT approval for Level 3 milestones

* no approval is needed for Level 4 milestones, however any non-trivial change need to be communicate
  within the DM team

* trivial changes, such as small corrections / clarifications to narrative that do not affect
  scope, time or budget are allowed without approval.

Typically, adjustments to Level 1, 2 and 3 milestons are made every 6 or 12 months. Changes to Level 4
milestones can occur more frequently.

Short-term Planning
-------------------

Short-term Plan is managed through *epics* and *stories*, and executed through *cycles*.

In the EVMS world, epics map directly to *activities*, and stories map to *activity steps*.

Epics and Stories
~~~~~~~~~~~~~~~~~

Typically, Planning Packages emcompass large blocks of work. To plan and execute work in details,
finer-grain planning is required. This is implemented through epics and stories.

Each epic captures a non-trivial work that is associated with a subset of work defined in a
Planning Package. Each epic has a clear description, well defined deliverables, and
relationships with a Planning Package (an epic *implements* a PP), and a Milestone (an epic
*blocks* a milestone). Epics are resources loaded, and have start and end dates defined.

Each epic is broken into smaller chunks of work, called *Stories*. Stories are primarily used
to define and manage short-term activities of individual developers.

Epics and stories are used to track all software work, as well as work on delivering hardware and
services that are tightly coupled with software (example: "Deliver OpenStack-based Test Cluster
running RedHat 6.1".) Details of work on stand-alone activities do not have to be captured on daily bases
through stories (example: "Deliver 10Gbit link between Chile and USA")

.. _cycles-and-releases:

Cycles and Releases
~~~~~~~~~~~~~~~~~~~

The work is executed through 6-month *cycles*. Scope of work for each cycle is driven by the Baseline
Plan, in particular by milestones. Each cycle ends with a new software release. Releases are
thorougly tested and documented.

Cycles are planned through *epics*. Each epic must be defined such that it can be completed
within a single cycle.

Once a plan is defined for a given cycle, it is loaded into PMCS and changed-controlled. A plan for
a cycle is loaded to PMCS during the month proceeding the start of the cycle.

Any non-trivial adjustements to the plan that affect scope, schedule or budget must be approved
by CCB.

It is acceptable to load the plan in 3-month chunks, e.g., the plan for
the first 3 months of the cycle is loaded before the start of the cycle, and the remaining
part of the plan covering the last 3 months is loaded before the 4th month starts. This
allows for minor fine-tuning of the second half of the cycle without going through the CCB
approval.

Epics-based Long-term Planning
------------------------------

As explained above, epics are used for planning and executing work within a cycle.

In addition to that, epics are also extremely valuable for longer-term planning at a fine-grain level.
When details of work for a given planning package are known, they can and should be captured through
epics. Such epics can be freely created and changed at any time without any approvals. They
should, of course, fit within the scope and budget of related PP. They can be useful for
bottom-up analysis and validation of resources needed to implement a given PP. This allows
to do detailed planning in flexible and agile way, while ensuring the scope/cost/schedule is
well controlled and managed.

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

A small fraction of all DM labor is performed by Contractors. The contractor labor is managed as LOE,
directly in dollars.

People
======

* DM Project Manager responsible for overall plan, schedule and priorities.

* Work divided into smaller pieces, through WBS.

* Each piece has a dedicated technical manager.

* Main responsibilites of technical managers:

  * Assemble the team capable of delivering work scoped through the WBS on-time and within budget.
    Provide daily technical management and leadership for the team, monitor and optimize team performance.

  * Work closely with the DM Project Manager on defining short and long-term plan and schedule for
    their teams. Direct the execution of their teams's plan, ensuring the team delivers on-time and within budget.

  * Report group's activities as required, including reporting to the Earned Value Management System (EVMS)
    used by LSST, and providing input for monthly status reports.

* In a sense, DM PM "owns" the overall baseline plan (PPs, milestones), and technical manager "own" epics.


Tools
=====

Master copy of the Baseline Plan, which includes all planning packages and all
milestones is captured in Primavera. A copy of that information is kept in JIRA
DLP project. It is periodically synchronized with Primavera.

Master copy of Epics and Stories is kept in JIRA in DM project. The snaphot for
epics corresponding to current and upcoming Cycle is taken and kept in Primavera.

Information in JIRA for current Cycle is particularly important, it needs to be
kept up-to-date and it should reflect the current state of the progress. Progress
updates for activities that block other teams, in particular when the delivery date
approaches are expected to be done promptly (depending on urgency, weekly or even daily)

Keeping a copy Baseline Plan in JIRA is in particular useful for linking the PPs
with corresponding Epics.

The JIRA DLP serves as an easy-to-use interface TCAMs can use to interact with
the Baseline Plan. Changes made to the JIRA DLP are periodically submitted to CCB
and transfered to the Primavera once approved (every 6 or 12 month). Primavera
version is always the authoritative source of truth.


Everything below is for Technical Note / how to
===============================================

.. WARNING::
   Everything below needs a lot of cleanup

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

For a typical full-time developer:

* 1800 h/year to allow for vacation, sick, holidays, --> 150 h per month

* applying 30% overhead for meetings, ad-hoc discussions and various interruptions

* left: 26.3 4-hour blocks (150*(1-30%)/5). These are considered "pure, interrupted blocks", which we call "story points". So, 1 FTE-month = 26.3 SPs

* adjustments are made depending on actual availability, for example

  - a developer working at 50% will have ~13 SPs available in a month

  - a TCAM who spends ~50% on managing the team will have 50%*(1-30%)*26.3 SPs available for pure, interrrupted work

  - scientists will typically spend 20% of their time on doing science, so a full time scientist will have 80% x 26.2 SPs available for coding.


Cross-team work
---------------

* developers from team A can be assigned to work under WBS that belongs to team B, both TCAMs need to agree. If known ahead of time, it should be captured in the plan and resources from team A should be assigned to WBS of team B.
* TCAMs can occasionally "trade" small pieces of work.

Resource loading for bugs
-------------------------

.. warning::

  this needs thinking

There are two schools:

* bugs should have story points. This helps to understand real velocity

* bugs should not have stories points because developers already earned value for completing the story that led to the bug, and they should not receive more points for it, they shouldn't have earned the points to begin with

(need to decide, Camera Team does the later. I am leaning towards the former, reserving reasonable number of story points in the long-term plan for bug fixes, carefully tracking story points used for bug fixes in each cycle, and adjusting the planned number of story points for bug fixes in future cycles based on findings)

Related reading:

* http://programmers.stackexchange.com/questions/162145/story-points-for-bug-fixing-tasks-is-it-suitable-for-scrum

* http://www.infoq.com/news/2011/01/story-points-to-bugs


Special Cases
-------------

In some cases work can not be easily defined up front (for example, user support). For these cases, only an epic with clearly defined resources are allocated in each cycle. These resources are then used to perform work. Decisions which activities are done as part of current cycle, which activities are assigned to such epics in future cycles, and which activities have too-low priority to be fit into any of these epics are made while a cycle is in progress.

Similar technique is applied for activities that require scientific research, which is often impossible to accurately predict. In the case of scientific research, clearly defined milestones are defined on the way to ensure progress is made as planned.


Tracking Late Work
------------------

In situations where work defined in an epic has not been completed and the cycle comes to an end, the epic must be kept ("in progress"), e.g., it should not be marked "Done" until all the work covered through that epic has been completed. The cycle field should be appropriately adjusted to reflect when the epic will be worked on, typically it will be next cycle (but it does not have to be. Such epic will be triggering schedule variance for as long as the work is not complete and until the epic is marked "Done".


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

* Need ot iscuss when to add new story to existing epic, when to add new epic, is if ever okay to change a story etc


Tools
-----

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


Jeff mentioned that "Linked epic-based tool does not provide latest full LDM-240 table view (i.e. for all WBS, by WBS, by cycle (not FY)).  Make sure other scripts work for this and dependency graph views."


JIRA
~~~~

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

* standalone non-software activities and LOE not reflected by epics and stories in JIRA DM, only in JIRA DLP and PMCS.

JIRA / PMCS Integration
~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

  Kevin, please help us fill this section


* Plan loaded to PMCS before cycle starts. Information used: epics keys, descriptions, story points, wbs

* Snapshot taken monthly:

 - start of epics ("epic status changed from "to do" to "in progress" or "done")

 - completed epics (epics marked "Done")

 - completed epics (stories marked "done")



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
~~~~

(short descr what it gives us)


Custom Tools
~~~~~~~~~~~~

(mention eCAM)

mention spreadsheet
 - can drill down ...

Reporting Process
-----------------

Reuse http://developer.lsst.io/en/latest/processes/project_planning.html#data-management-reporting-process

Introduce:

* monthly cycle reports, 5 min/team, all hands, virtual, plus short discussion

* cycle introduction meeting 15 min per team, right when cycle starts, ahm, virtual
