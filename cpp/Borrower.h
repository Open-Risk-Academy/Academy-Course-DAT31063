#ifndef BORROWER_H
#define BORROWER_H

#include <string>

/**
  * class Borrower
  * 
  */

/******************************* Abstract Class ****************************
Borrower does not have any pure virtual methods, but its author
  defined it as an abstract class, so you should not use it directly.
  Inherit from it instead and create only objects from the derived classes
*****************************************************************************/

class Borrower {

    public:

      // Constructors/Destructors
      //


      /**
       * Empty Constructor
       */
      Borrower ();

      /**
       * Empty Destructor
       */
      virtual ~Borrower ();

      // Static Public attributes
      //

      // Public attributes
      //


      // Public attribute accessor methods
      //


      // Public attribute accessor methods
      //


    protected:

      // Static Protected attributes
      //

      // Protected attributes
      //

    public:


      // Protected attribute accessor methods
      //

    protected:

    public:


      // Protected attribute accessor methods
      //

    protected:


    private:

      // Static Private attributes
      //

      // Private attributes
      //

      // The name of the Borrower
      std::string name;
    public:


      // Private attribute accessor methods
      //

    private:

    public:


      // Private attribute accessor methods
      //


      /**
       * Set the value of name
       * The name of the Borrower
       * @param new_var the new value of name
       */
      void setName (std::string new_var)   {
          name = new_var;
      }

      /**
       * Get the value of name
       * The name of the Borrower
       * @return the value of name
       */
      std::string getName ()   {
        return name;
      }
    private:


      void initAttributes () ;

};

#endif // BORROWER_H
