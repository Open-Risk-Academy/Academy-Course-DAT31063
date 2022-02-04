#ifndef PRIVATEBORROWER_H
#define PRIVATEBORROWER_H
#include "Borrower.h"

#include <string>

/**
  * class PrivateBorrower
  * 
  */

class PrivateBorrower : public Borrower {

    public:

      // Constructors/Destructors
      //


      /**
       * Empty Constructor
       */
      PrivateBorrower ();

      /**
       * Empty Destructor
       */
      ~PrivateBorrower ();

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

      // The annual income of a person
      float annual_income;
    public:


      // Private attribute accessor methods
      //

    private:

    public:


      // Private attribute accessor methods
      //


      /**
       * Set the value of annual_income
       * The annual income of a person
       * @param new_var the new value of annual_income
       */
      void setAnnual_income (float new_var)   {
          annual_income = new_var;
      }

      /**
       * Get the value of annual_income
       * The annual income of a person
       * @return the value of annual_income
       */
      float getAnnual_income ()   {
        return annual_income;
      }
    private:


      void initAttributes () ;

};

#endif // PRIVATEBORROWER_H
