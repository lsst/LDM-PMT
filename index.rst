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

.. _intro:

Introduction
============

* LSST construction, complex software, large team, long time

* need robust process to plan, to maintain the plan, to track progress and fully execute the plan

* need detailed, realistic resource-loaded, long-term plan covering entire construction

* funded under NSF MREFC, process needs to be formal


People
======

* DM Project Manager responsible for overall plan, schedule and priorities.

* Delegates to TCAMs work within the teams they manage

TCAMs Roles:

* come up with up to date long term plan for the team

* maintain the plan: adjust to changing needs, replan as resource availability changes

* come up with detailed, resouce loaded plan for each upcoming cycles

* executing the short term plan, typically through sprints


.. _planning-process:

Planning Process
================

.. _methodology:

Planning Methodology
--------------------

Top down and bottom up, periodically re-synchronizing both.

* top-down plan produced at the beginning of construction [footnote: major overhaul undertaken 1 1/2 year after start of construction]

* bottm up updated continuously

* top-down / bottom up resynchronized annually, exported to LDM-240, that becomes an official baseline


.. _topdown:

Top down
~~~~~~~~

* project-level requirements, risks

* dm requirements (dpdd, ...)

* baseline architecture (apps, middleware, db, infra model...)

  - covers all requirements

  - discusses what features are part of baseline, and which are out of scope

* project-level milestones

* dm milestones

  - cover entire construction period

  - every non-trivial part of the baseline architecture have at least one milestone

  - o(several hundred) milestones

  - dividing into two categories: externally visible, an internal

    + externally visible, every attempt is made to keep them as stable as possible

    + internal milestones are more flexible

      - for internal milestones, keep track of early customers that need them

      - if we need to push milestones for later, we know who to check with and negotiate


.. _bottomup:

Bottom up
~~~~~~~~~

* track every piece of work, every task, every non-trivial activity that needs to be done during construction along with resources

* keep track of which part of baseline each piece of work addresses

* keep track which piece of work blocks which milestone

* it should always reflect reality

  - change it as a need arises (agile), and get CCB approval for resource/scope change


.. _middlefield:

Middlefield
~~~~~~~~~~~

* re-sync bottom-up with to-down and refresh the baseline long-term resource-loaded plan once a year


.. _cycles-and-releases:

Cycles and Releases
-------------------

* All work divided into 6-month "cycles"

* each cycle produces a "release", sprint (Nov-Apr), fall (May-Oct)

  - official QA, come with documentation

* scope and priorities driven by the baseline long term plan

* setting priorities, exact scope and order of work is ultimately the responsibility of the DM Project Manager


.. _cycle-planning:

Cycle Planning
--------------

* plan all 6 months

  - detailed plan, resource loaded

  - (describe spreadsheet here)

* loading 3

* fine-tuning, load the rest in 2nd month + LCR

* building realistic plan

  - not adding any *artificial* padding or buffers

  - reserving time for expected problems/bugs/issues

  - each piece of work clearly defined, scoped, with clear deliverables, not just "continue doing x"

    + research activities time-boxed

  - Reserving time to do exploration and research necessary to well understand scope / resource-load work planned for cycle x+1.

  - Reserving time for cross-team discussions (recommended ~2-3 days per each team pair)

  - Reserving time for documentation, recommended 1-2 week sprint at the beginning of cycle to
    bring all documentation up to date with the work done in previous cycle

* while doing cycle plan, combing through the list of all work during cycle planning, reordering as needed

* plan is verified and issues such overloaded developers are caught

* plan captures all non-LOE activities


Resource loading a cycle
------------------------

* 1800 h/year

* xx per month

* adjusting to capture LOE time, eg, tcam spending 50% on non-coding

* Adjusting to capture science time (20%)

* applying 30% overhead for ...

* left: xx h, = xx story points per FTE-month

* 1 FTE-month = 26 SPs, 50% TCAM = 13 SPs

* ok to show LOE activities but should not be part of epics with cycle (tracked by PMCS)

* team --> story pool

* assigning available story points per developer


Resource loading for bugs
-------------------------

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

* we will be looking at burndown charts every month


Keeping Plan Up-to-date
-----------------------

In JIRA:

* have defined epics for every major piece of work, assigned estimated story points

* as we learn more, fine-tune design, we

  - improve the epics:

    + add more detailed description

  - define stories

    + fine tune story points (that might change resources needed)

* occasionally requirements might change, or we might discovered the plan is missing a feature

  - this might lead to creating new epics, or deleting existing epics

* every time that happens, revisit overall plan to make sure it is not overloaded.

* rebalance

* attempting to avoid disrupting milestones, in particular the externally visible milestones

* each change to scope of resources must be approved by CCB

* so, the plan in PMCS is agile, always reflects true, most up-to-date state

* allows developers to feel unconstraint by the rigidness of PMCS


Monitoring
-----------

* scripts for monitoring / flagging / alerting

  - mark epics in progress when stories in progress/done

  - sum of story points for all stories in epic significantly differs for epic SP estimate

  - stories in progress for too long

  - stories too large

  - too many stories per developer in a month

  - etc


Tools
=====

* JIRA DM project

  - tracks all non-LOE software work

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


Reporting Process
=================

Reuse http://developer.lsst.io/en/latest/processes/project_planning.html#data-management-reporting-process

Introduce:

* monthly cycle reports, 5 min/team, all hands, virtual, plus short discussion

* cycle introduction meeting 15 min per team, right when cycle starts, ahm, virtual
