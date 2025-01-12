import { createContext, ReactNode, useContext, useEffect, useState } from "react";
import { getAvailableModels } from "@/services/models";
import { useDiffusion } from "./SDContext";
import { ModelCategory } from "./ModelsContext";

export interface IControlNetContext {
  controlNetModels: any[];
  selectedCNModel: string;
  setSelectedCNModel: (model: string) => void;
  controlNetType: string;
  setControlNetType: (controlNetType: string) => void;
  buildControlNetPrompt: () => any;
}

const initialConfig = {
  selectedCNModel: "lllyasviel/sd-controlnet-canny",
  controlNetType: "canny",
};

const defaultState = {
  controlNetModels: [],
  selectedCNModel: initialConfig.selectedCNModel,
  setSelectedCNModel: () => {},
  controlNetType: initialConfig.controlNetType,
  setControlNetType: () => {},
  buildControlNetPrompt: () => {},
};

const ControlNetContext = createContext<IControlNetContext>(defaultState);

const ControlNetProvider = (props: { children: ReactNode }) => {
  const { buildPrompt } = useDiffusion();
  // ControlNet Models
  const [controlNetModels, setControlNetModels] = useState<any>([]);
  const [selectedCNModel, setSelectedCNModel] = useState<string>(initialConfig.selectedCNModel);
  const [controlNetType, setControlNetType] = useState<string>(initialConfig.controlNetType);

  useEffect(() => {
    // Fetch ControlNet models
    async function getControlNetModels() {
    const response = await getAvailableModels("/models");
    if (response.success && response.data) {
      const filteredModels = response.data.filter((model: any) =>
        model.categories.some((category: any) => category.name === ModelCategory.Processing)
      );
      setControlNetModels(filteredModels || []);
    }
  }
    getControlNetModels();
  }, []);

  const buildControlNetPrompt = () => {
    const promptObject = buildPrompt();
    return {
      ...promptObject,
      controlnet_model: selectedCNModel,
      controlnet_type: controlNetType,
    };
  };

  return (
    <ControlNetContext.Provider
      value={{
        controlNetModels,
        selectedCNModel,
        setSelectedCNModel,
        controlNetType,
        setControlNetType,
        buildControlNetPrompt,
      }}
    >
      {props.children}
    </ControlNetContext.Provider>
  );
};

const useControlNet = () => {
  const context = useContext(ControlNetContext);
  if (context === undefined) {
    throw new Error("useDiffusion must be used within a DiffusionProvider");
  }
  return context;
};

export { ControlNetProvider, useControlNet };
