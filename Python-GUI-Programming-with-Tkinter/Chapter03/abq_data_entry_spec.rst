======================================
 ABQ Data Entry Program specification
======================================


Description
-----------
The program is being created to minimize data entry errors for laboratory measurements.

Functionality Required
----------------------

The program must:

* allow all relevant, valid data to be entered, as per the field chart
* append entered data to a CSV file
  - The CSV file must have a filename of abq_data_record_CURRENTDATE.csv,
    where CURRENTDATE is the date of the checks in ISO format (Year-month-day)
  - The CSV file must have all the fields as per the chart
* enforce correct datatypes per field

The program should try, whenever possible, to:

* enforce reasonable limits on data entered
* Auto-fill data
* Suggest likely correct values
* Provide a smooth and efficient workflow

Functionality Not Required
--------------------------

The program does not need to:

* Allow editing of data. This can be done in LibreOffice if necessary.
* Allow deletion of data.

Limitations
-----------

The program must:

* Be efficiently operable by keyboard-only users.
* Be accessible to color blind users.
* Run on Debian Linux.
* Run acceptably on a low-end PC.

Data Dictionary
---------------
+------------+----------+------+------------------+--------------------------+
|Field       | Datatype | Units| Range            |Descripton                |
+============+==========+======+==================+==========================+
|Date        |Date      |      |                  |Date of record            |
+------------+----------+------+------------------+--------------------------+
|Time        |Time      |      |8:00, 12:00,      |Time period               |
|            |          |      |16:00, or 20:00   |                          |
+------------+----------+------+------------------+--------------------------+
|Lab         |String    |      | A - E            |Lab ID                    |
+------------+----------+------+------------------+--------------------------+
|Technician  |String    |      |                  |Technician name           |
+------------+----------+------+------------------+--------------------------+
|Plot        |Int       |      | 1 - 20           |Plot ID                   |
+------------+----------+------+------------------+--------------------------+
|Seed        |String    |      |                  |Seed sample ID            |
|sample      |          |      |                  |                          |
+------------+----------+------+------------------+--------------------------+
|Fault       |Bool      |      |                  |Fault on environmental    |
|            |          |      |                  |sensor                    |
+------------+----------+------+------------------+--------------------------+
|Light       |Decimal   |klx   | 0 - 100          |Light at plot             |
+------------+----------+------+------------------+--------------------------+
|Humidity    |Decimal   |g/m³  | 0.5 - 52.0       |Abs humidity at plot      |
+------------+----------+------+------------------+--------------------------+
|Temperature |Decimal   |°C    | 4 - 40           |Temperature at plot       |
+------------+----------+------+------------------+--------------------------+
|Blossoms    |Int       |      | 0 - 1000         |Number of blossoms in plot|
+------------+----------+------+------------------+--------------------------+
|Fruit       |Int       |      | 0 - 1000         |Number of fruits in plot  |
+------------+----------+------+------------------+--------------------------+
|Plants      |Int       |      | 0 - 20           |Number of plants in plot  |
+------------+----------+------+------------------+--------------------------+
|Max height  |Decimal   |cm    | 0 - 1000         |Height of tallest plant in|
|            |          |      |                  |plot                      |
+------------+----------+------+------------------+--------------------------+
|Min height  |Decimal   |cm    | 0 - 1000         |Height of shortest plant  |
|            |          |      |                  |in plot                   |
+------------+----------+------+------------------+--------------------------+
|Median      |Decimal   |cm    | 0 - 1000         |Median height of plants in|
|height      |          |      |                  |plot                      |
+------------+----------+------+------------------+--------------------------+
|Notes       |String    |      |                  |Miscellaneous notes       |
+------------+----------+------+------------------+--------------------------+

inman
-----
.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``correct_map``
     - dict
     - For each problem ID value listed by ``answers``, provides:

       * ``correctness``: string; 'correct', 'incorrect'
       * ``hint``: string; Gives optional hint. Nulls allowed.
       * ``hintmode``: string; None, 'on_request', 'always'. Nulls allowed.
       * ``msg``: string; Gives extra message response.
       * ``npoints``: integer; Points awarded for this ``answer_id``. Nulls allowed.
       * ``queuestate``: dict; None when not queued, else ``{key:'', time:''}``
         where ``key`` is a secret string dump of a DateTime object in the form
         '%Y%m%d%H%M%S'. Nulls allowed.

   * - ``grade``
     - integer
     - Current grade value.
   * - ``max_grade``
     - integer
     - Maximum possible grade value.

.. math:: \sigma_\mathrm{mean} = \frac{\sigma}{\sqrt{N}}
   :label: math-sample

.. math::

   \nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}

   \nabla \cdot \mathbf{B} = 0

.. math::

   x &= (a + b)^2 \\
     &= a^2 + 2ab + b^2