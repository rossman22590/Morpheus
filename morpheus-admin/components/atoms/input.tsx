import { ComponentPropsWithoutRef } from "react";

interface TextInputProps extends ComponentPropsWithoutRef<"input"> {
  label: string;
  register: any;
  validationSchema?: any;
  errors?: any;
  value?: string;
}

export const TextInput = (props: TextInputProps) => {
  const getInputError = () => {
    if (!props.errors) return null;
    if (props.errors.type === "required") return "This field is required";
    if (props.errors.type === "minLength") return "Min length is 5";
    if (props.errors.type === "maxLength") return "Max length is 20";
  };

  return (
    <div className="w-full form-control">
      <label className="label">
        <span className="label-text">
          {props.label} {props.validationSchema.required && "*"}
        </span>
      </label>

      <input
        name={props.name}
        value={props.value}
        type={props.type || "text"}
        placeholder={props.placeholder}
        className="w-full input input-bordered"
        {...props.register(props.name, props.validationSchema)}
      />

      {props.errors && (
        <label className="label">
          <span className="text-sm error text-error">{getInputError()}</span>
        </label>
      )}
    </div>
  );
};
